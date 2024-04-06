#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.srv import TjenesteOblig5
from time import sleep
from std_msgs.msg import String

import RPi.GPIO as GPIO

class KlientNode(Node):
    def __init__(self):
        super().__init__('brytermonitor')
        self.cli = self.create_client(TjenesteOblig5, 'oblig5')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            print('Tjeneste utilgjengelig, venter...')


    def send_request(self):
        knapp_pinin = 27
        knapp_pinut = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(knapp_pinin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(knapp_pinut, GPIO.OUT)
        GPIO.output(knapp_pinut, GPIO.HIGH)

        while True:
            tilstand = GPIO.input(knapp_pinin)
            request = TjenesteOblig5.Request()
            request.bryter_id = tilstand
            self.future = self.cli.call_async(request)
            rclpy.spin_until_future_complete(self, self.future)
            global result
            result = self.future.result()
            min_instans = MinimalPublisher()
            print(result.result)
            result = result.result
            min_instans.status()
            rclpy.spin_once(min_instans, timeout_sec=0.1)
            sleep(1)


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("geris3014_send_bryter_status")
        self.publisher = self.create_publisher(String, "bryter_status", 25)

    def status(self):
        global result
        msg = String()
        msg.data = f'{result}'
        self.publisher.publish(msg)

def main():
    try:
        rclpy.init()
        klient = KlientNode()
        while rclpy.ok():
            klient.send_request()
    except KeyboardInterrupt:
        print('\nStoppa av brukaren.')
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
