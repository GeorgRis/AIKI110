#!/usr/bin/env python3
import re

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):
    def __init__(self):
        global lr
        super().__init__("geris3014lytter_node")
        lr = []
        self.subscription = self.create_subscription(
            String,
            "chatter",
            self.lytter_callback,
            25)

    def lytter_callback(self, string_data):
        global lr
        mottatt = string_data.data
        lr.append(re.findall('\d+',mottatt))
        print("Mottok: %s" % mottatt)

def main():
    global lr
    i = 0
    rclpy.init()
    min_instans = MinimalSubscriber()
    while i < 13:
        rclpy.spin_once(min_instans, timeout_sec=1)
        i += 1

    komprimertlr = []
    for liste in lr:
        for item in liste:
            komprimertlr.append(item)

    count = dict()
    for i in komprimertlr:
        count[i] = count.get(i, 0) + 1
    count.pop('3014')
    f = open("/aiki110/home/geris3014/ros2_ws/src/geris3014oblig2/geris3014oblig2/skriv.txt", 'w')
    f.write(str(count))
    print(count)
    f.close()
    min_instans.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()