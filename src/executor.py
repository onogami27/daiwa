import time
from .video_reader import VideoReader


class Executor:
    def __init__(self):
        pass

    def execute(self):
        camera_id = 0
        video_reader = VideoReader(camera_id)

        video_reader.execute()

