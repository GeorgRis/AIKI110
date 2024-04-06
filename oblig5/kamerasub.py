#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.msg import RawHuedata
import numpy as np
import cv2 as cv

class Bildebehandler(Node):
    def __init__(self):
        super().__init__('bildebehandler_node')
        self.subscription = self.create_subscription(RawHuedata, 'kamera', self.callback, 10)

    def callback(self, msg):
        hue_bytes = msg.data
        image = np.ndarray((480, 640), np.uint8, hue_bytes)
        cv.imwrite("hue.jpg", image)


