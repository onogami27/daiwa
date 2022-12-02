from multiprocessing.spawn import old_main_modules
import cv2
from cv2 import aruco
import numpy as np
import time
import datetime
import math

from models.ar_marker import ArMarkerPoint
from serial_sender import SerialSender

W_H = 320
H_H = 240
MARGIN = 50
HEIGHT_LIMIT = 350

FONT = cv2.FONT_HERSHEY_SIMPLEX
POSITION = (10, 450)
FONT_SCALE = 2
FONT_COLOR = (255, 255, 0)


class VideoReader:
    def __init__(self, camera_id):
        self.camera = cv2.VideoCapture(camera_id)
        self.serial_sender = SerialSender()
        self.status = 0

        self.available_point_counts = [1, 4]

        # aruco設定
        self.ar_marker_ids = [0, 2, 3, 4, 5, 6]
        self.output_path = "./read_ar_marker_logs.csv"
        self.dict_aruco = aruco.Dictionary_get(aruco.DICT_APRILTAG_36h11)
        self.parameters = aruco.DetectorParameters_create()

    def execute(self):
        """
        カメラを起動し、指定したar_marker
        """
        while True:
            line = self.serial_sender.read()
            if line:
                try:
                    l_pow = int(line[10:15])
                    r_pow = float(line[18:23])

                    with open(output_path, mode="a") as f:
                        row_data = f'{l_pow},{","},{r_pow}\n'
                        f.write(row_data)

                    self.serial_sender.send(row_data)
                    # self.status = int(read_data)
                    
                except:
                    pass

            markers, frame = self._read_mark_id_points()  # フレームを取得
            self._show_line(frame)

            if self.status == 0:
                # 読み取ったar_markerの数が有効数である場合、シリアル通信を送信する
                if self._is_available_point_counts(markers):
                    point_w = self._send_serial_by_ar_marker_points(markers)
                    cv2.putText(frame, point_w,
                                POSITION,
                                FONT,
                                FONT_SCALE,
                                FONT_COLOR, 3, cv2.LINE_AA, True)

            if self.status == 1:
                print("status 1")

            #cv2.imshow("camera", frame)  # フレームを画面に表示

            # キー操作があればwhileループを抜ける
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            
            return markers,frame

        # カメラオブジェクトとウィンドウの解放
        #self.camera.release()
        #self.serial_sender.close()
        #cv2.destroyAllWindows()

    def _send_serial_by_ar_marker_points(self, read_ar_marker_points):
        """読み取ったar_markerのidに応じてシリアル通信を送信する"""
        if len(read_ar_marker_points) == 1:
            return self._send_serial_when_single_ar_marker_id(read_ar_marker_points[0])
        if len(read_ar_marker_points) == 4:
            return self._send_serial_when_multi_ar_marker_points(read_ar_marker_points)

        return ''

    @staticmethod
    def _show_line(frame):
        cv2.line(frame, (0, HEIGHT_LIMIT), (640, HEIGHT_LIMIT), (0, 0, 255), 1)
        cv2.line(frame, (W_H, 0), (W_H, 480), (255, 0, 0), 1)
        cv2.line(frame, (W_H + MARGIN, 0), (W_H + MARGIN, 480), (0, 255, 0), 2)
        cv2.line(frame, (W_H - MARGIN, 0), (W_H - MARGIN, 480), (0, 255, 0), 2)

    def _read_mark_id_points(self):
        """
        静止画を取得し、arucoマークのidリストを取得する
        """
        ret, frame = self.camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        corners, ids, rejected_img_points = aruco.detectMarkers(gray, self.dict_aruco, parameters=self.parameters)

        if ids is None:
            return [], frame

        read_ids = np.ravel(ids)

        if not self._is_available_point_counts(read_ids):
            return [], frame

        read_ar_marker_points = []

        for read_id in read_ids:
            index = np.where(ids == read_id)[0][0]
            corner_points = corners[index][0]
            ar_marker_point = ArMarkerPoint(read_id, corner_points)

            read_ar_marker_points.append(ar_marker_point)

        read_ar_marker_points = sorted(read_ar_marker_points)

        return read_ar_marker_points, frame

    @staticmethod
    def _calc_from_points(ar_marker_point: ArMarkerPoint):
        # 底辺
        width = ar_marker_point.left_top[0] - ar_marker_point.right_top[0]  # 左上X - 右上X
        center_width = ar_marker_point.left_top[0] + width / 2
        # 高さ
        height = ar_marker_point.right_top[1] - ar_marker_point.left_top[1]  # 右上ｙ-左上ｙ
        center_height = ar_marker_point.left_top[1] + height / 2

        # 底辺と高さから角度を求める
        angle = round(math.atan(height / width) * 180 / math.pi)
        # 底辺と高さから斜辺を求める
        hypotenuse = round(math.sqrt(math.pow(width, 2) + math.pow(height, 2)))

        return center_width, center_height, angle, hypotenuse

    @staticmethod
    def _get_command_by_angle(angle):
        """ar_markerの角度からコマンドを取得する"""
        if angle > 3:
            command = 'l'
        elif angle < -3:
            command = 'r'
        else:
            command = ' '

        return command

    def _is_available_point_counts(self, ar_marker_points):
        """ar_markerのidが読み取り数が有効数であるかどうかを判定する"""
        return len(ar_marker_points) in self.available_point_counts

    def _send_serial_when_single_ar_marker_id(self, ar_marker_point):
        center_width, center_height, angle, hypotenuse = self._calc_from_points(ar_marker_point)
        command = self._get_command_by_angle(angle)

        if HEIGHT_LIMIT > center_height:
            if center_width > W_H + MARGIN:
                point_w = "L_TURN"
            elif center_width < W_H - MARGIN:
                point_w = "R_TURN"
            else:
                point_w = "CENTER"
        else:
            point_w = "STOP"

        print(angle, hypotenuse, point_w)
        # self.serial_sender.send(point_w)  # TODO serial通信をする時はコメントアウトを解除する

        return point_w

    def _send_serial_when_multi_ar_marker_points(self, ar_marker_points):
        ar_marker_ids = [str(marker.ar_marker_id) for marker in ar_marker_points]
        ser_command = "".join(ar_marker_ids)
        with open(self.output_path, mode="a") as f:
            now = datetime.datetime.now()
            row_data = f'{now.strftime("%Y/%m/%d")},{now.strftime("%H:%M:%S")},{",".join(ar_marker_ids)}\n'
            f.write(row_data)

        c_len = 16 - len(ser_command)
        out_command = ser_command + "0" * c_len
        # self.serial_sender.send(out_command)  # TODO serial通信をする時はコメントアウトを解除する
        print(out_command)

        return out_command

