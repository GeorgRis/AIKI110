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


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("geris3014_kamera_node")
        self.publisher = self.create_publisher(String, "geris3014_status", 25)

    def status(self):
        msg = String()
        msg.data = f'OK'
        self.get_logger().info('Kamera_status"%s"' % msg.data)
        self.publisher.publish(msg)


def main():
    rclpy.init()

    min_instans = MinimalPublisher()

    try:
        min_instans.status()
        rclpy.spin(min_instans)
    except KeyboardInterrupt:
        print('Stoppa av bruker')
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
