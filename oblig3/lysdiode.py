#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep


import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def lys():
    led_pin = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("geris3014_lys_node")
        self.subscription = self.create_subscription(
            String,
            "geris3014_status",
            self.lytter_callback,
            25)

    def lytter_callback(self, string_data):
        motatt = string_data.data
        print("Kamera: %s" % motatt)
        if motatt == 'OK':
            lys()


def main():
    rclpy.init()

    min_instans = MinimalSubscriber()
    try:
        rclpy.spin(min_instans)
    except:
        print("Stoppa av bruker")
    finally:
        lys()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
