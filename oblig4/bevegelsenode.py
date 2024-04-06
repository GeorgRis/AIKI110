#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("geris3014_bevegelse_node")
        self.subscription = self.create_subscription(
            String,
            "bryter_status",
            self.lytter_callback,
            25)

    def lytter_callback(self, string_data):
        motatt = string_data.data
        if motatt == '1':
            print("kjører")
            min = MinimalPublisher()
            min.status()
            rclpy.spin_once(min, timeout_sec=0.1)

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("geris3014_send_kjore_status")
        self.publisher = self.create_publisher(String, "kjore_status", 25)

    def status(self):
        msg = String()
        msg.data = f'1'
        self.publisher.publish(msg)

def main():
    rclpy.init()
    min_instans = MinimalSubscriber()
    try:
        rclpy.spin(min_instans)
    except:
        print("Stoppa av bruker")
    finally:
        pass

if __name__ == '__main__':
    main()