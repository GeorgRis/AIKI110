import rclpy
from rclpy.node import Node
from interfaces.msg import RawHuedata
from picamera2 import Picamera2
import cv2 as cv
import numpy as np

class KameraNode(Node):
    def __init__(self):
        super().__init__('kamera_node')
        self.camera = Picamera2()
        config = self.camera.create_preview_configuration({'format':'RGB888'})
        self.camera.configure(config)
        self.camera.start()
        self.publisher = self.create_publisher(RawHuedata, 'kamera', 10)
        self.timer = self.create_timer(1, self.timer_callback)


    def timer_callback(self):
        img = self.camera.capture_array()
        image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        hue, saturation, value = cv.split(image_hsv)
        hue_bytes = hue.tobytes()

        msg = RawHuedata()
        msg.data = hue_bytes
        self.publisher.publish(msg)