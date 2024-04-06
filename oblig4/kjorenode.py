#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from time import sleep
from std_msgs.msg import String
import RPi.GPIO as GPIO

lf_pin = 19
rf_pin = 13
rb_pin = 6
lb_pin = 26
lys_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(lf_pin, GPIO.OUT)
GPIO.setup(rf_pin, GPIO.OUT)
GPIO.setup(rb_pin, GPIO.OUT)
GPIO.setup(lb_pin, GPIO.OUT)
GPIO.setup(lys_pin, GPIO.OUT)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("geris3014_kjore_node")
        self.subscription = self.create_subscription(
            String,
            "kjore_status",
            self.kjore,
            25)

    def kjore(self, string_data):
        motatt = string_data.data
        if motatt == '1':
            GPIO.output(lys_pin, GPIO.HIGH)
            sleep(1)
            GPIO.output(lys_pin, GPIO.LOW)
            rf_360()
            quit()


def rf_360():
    GPIO.output(rf_pin, GPIO.HIGH)
    sleep(0.81)
    GPIO.output(rf_pin, GPIO.LOW)


def main():
    rclpy.init()
    min_instans = MinimalSubscriber()
    try:
        rclpy.spin(min_instans)
    except:
        print("stoppa av bruker")
    finally:
        GPIO.output(rf_pin, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    main()