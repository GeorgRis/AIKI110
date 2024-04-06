import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("geris3014triller_node")
        self.publisher = self.create_publisher(String, "geris3014", 25)
        self.timer = self.create_timer(100, self.send)

    def send(self):
        kast = random.randint(1,19)
        msg = String()
        msg.data = f"Geris3014 trillet {kast} pa en D20"
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.publisher.publish(msg)


def main():
    i = 0
    rclpy.init()
    min_instans = MinimalPublisher()
    while i < 10:
        rclpy.spin_once(min_instans, timeout_sec=1)
        i += 1
    min_instans.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()