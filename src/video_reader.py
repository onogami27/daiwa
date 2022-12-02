from multiprocessing.spawn import old_main_modules
import cv2
from cv2 import aruco
import numpy as np
import time
import datetime
import math

# import valset

from models.ar_marker import ArMarkerPoint

w_h=320
h_h=240
mazin=50
hi_limt=350

font                   = cv2.FONT_HERSHEY_SIMPLEX
position               = (10,450)
fontScale              = 2
fontColor              = (255,255,0)

class VideoReader:
    def __init__(self, camera_id):
        self.camera = cv2.VideoCapture(camera_id)

        # aruco設定
        #self.ar_marker_ids = [0, 2, 3, 4, 5, 6]
        # self.output_path = './read_ar_marker_logs.txt'
        self.output_path = "ar_marker_logs.csv"
        self.dict_aruco = aruco.Dictionary_get(aruco.DICT_APRILTAG_36h11)
        # self.dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
        self.parameters = aruco.DetectorParameters_create()

    def execute(self):
        """
        カメラを起動し、指定したar_marker
        """
        while True:
            markers, frame, csv_data = self._read_mark_id_points()  # フレームを取得
            cv2.line(frame,(0,hi_limt),(640,hi_limt),(0,0, 255),1)
            cv2.line(frame,(w_h,0),(w_h,480),(255,0, 0),1)
            cv2.line(frame,(w_h+mazin,0),(w_h+mazin,480),(0,255, 0),2)
            cv2.line(frame,(w_h-mazin,0),(w_h-mazin,480),(0,255, 0),2)
            w_h+mazin
            #cv2.imshow("camera", frame)  # フレームを画面に表示

            #imshow(img)

            # キー操作があればwhileループを抜ける
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # カメラオブジェクトとウィンドウの解放
        #self.camera.release()
        #cv2.destroyAllWindows()

            return markers,frame,csv_data

    def _read_mark_id_points(self):
        """
        静止画を取得し、arucoマークのidリストを取得する
        """
        ret, frame = self.camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejected_img_points = aruco.detectMarkers(
            gray, self.dict_aruco, parameters=self.parameters
        )

        #マーカーのIDが検知されない時の処理
        if ids is None:
            return "", frame,""

        with open(self.output_path, mode="a") as f:
            read_ar_marker_points = []
            read_ids = np.ravel(ids)

            if len(read_ids) != 4 and len(read_ids) != 1:
                return [], frame

            for read_id in read_ids:
                index = np.where(ids == read_id)[0][0]
                corner_points = corners[index][0]
                ar_marker_point = ArMarkerPoint(read_id, corner_points)

                read_ar_marker_points.append(ar_marker_point)

                # if read_id in self.ar_marker_ids
                #     index = np.where(ids == read_id)[0][0]
                #     corner_points = corners[index][0]
                #     ar_marker_point = ArMarkerPoint(read_id, corner_points)

                #     read_ar_marker_points.append(ar_marker_point)

            read_ar_marker_points = sorted(read_ar_marker_points)
            now = datetime.datetime.now()

            # log=f'{now.strftime("%Y/%m/%d %H:%M:%S")} ar_marker_id:{[marker.ar_marker_id for marker in read_ar_marker_points]}'
            # log=f'{now.strftime("%Y/%m/%d")},{now.strftime("%H:%M:%S")},{[marker.ar_marker_id for marker in read_ar_marker_points]}'
            # log2=f'{now.strftime("%Y/%m/%d")},{now.strftime("%H:%M:%S")},{[marker.ar_marker_id for marker in read_ar_marker_points]}\n'
            #
            s_comand = f"{[marker.ar_marker_id for marker in read_ar_marker_points]}"
            cut_comand = s_comand.replace(" ", "")
            cut_comand = cut_comand.replace("[", "")
            CSV_data = cut_comand.replace("]", "")
            ser_comand = CSV_data.replace(",", "")
            CSV_data = f'{now.strftime("%Y/%m/%d")},{now.strftime("%H:%M:%S")},{CSV_data}\n'

            c_len = 16 - len(ser_comand)
            out_comand = ser_comand + "0" * c_len

            if len(read_ids) == 4:
                print(out_comand)
                f.write(CSV_data)
                #time.sleep(5)
                #シリアル０出力
            elif len(read_ids) == 1:
                # 底辺
                bottom = corner_points[0][0] - corner_points[1][0] #左上X-右上X
                c_w=corner_points[1][0]+bottom/2
                # 高さ
                height = corner_points[1][1] - corner_points[0][1] #右上ｙ-左上ｙ
                c_h=corner_points[0][1]+height/2
                m_h = corner_points[0][1] - corner_points[3][1] #左上ｙ-左下ｙ
                rote_h = corner_points[0][0] - corner_points[3][0] #左上X-左下X

                #[0][0]左上ｘ[0][1]左上y
                #[1][0]右上ｘ[1][1]右上y
                #[2][0]右下ｘ[2][1]右下y
                #[3][0]左下ｘ[3][1]左上y

                # 底辺と高さから角度を求める
                angle = round(math.atan(height / bottom) * 180 / math.pi)
                if angle > 3:

                    comand='l'
                elif angle < -3:
                    comand='r'
                else:
                    comand=' '

                # 底辺と高さから斜辺を求める
                hypotenuse = round(math.sqrt(math.pow(bottom, 2) + math.pow(height, 2)))
                if hi_limt>c_h:
                    if c_w>w_h+mazin :
                        point_w="L_turn"
                        cv2.putText(frame,'L_turn',
                            position,
                            font,
                            fontScale,
                            fontColor,3,cv2.LINE_AA, True)
                    elif c_w<w_h-mazin :
                        point_w="R_turn"
                        cv2.putText(frame,'R_turn',
                            position,
                            font,
                            fontScale,
                            fontColor,3,cv2.LINE_AA, True)
                    else:
                        cv2.putText(frame,'center',
                            position,
                            font,
                            fontScale,
                            fontColor,3,cv2.LINE_AA, True)
                        point_w="center"
                else:
                    cv2.putText(frame,'STOP',
                        position,
                        font,
                        fontScale,
                        fontColor,3,cv2.LINE_AA, True)
                    point_w="STOP"

                print(angle,hypotenuse,point_w)
                out_data = f"{angle} {hypotenuse} {point_w}"
                #print(hypotenuse)
                #シリアル１出力

                return out_data , frame, CSV_data

            else:
                return "", frame, CSV_data

        return read_ar_marker_points, frame, CSV_data


