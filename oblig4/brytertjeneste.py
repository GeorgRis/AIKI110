#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.srv import TjenesteOblig5 m

class TjenesteNode(Node):
    def __init__(self):
        super().__init__('brytertjeneste')
        self.srv = self.create_service(TjenesteOblig5,
                                        'oblig5',
                                        self.handle_TjenesteOblig5)

    def handle_TjenesteOblig5(self, request, response):
        response.result = request.bryter_id
        return response


def main():
    try:
        rclpy.init()
        tjeneste = TjenesteNode()
        rclpy.spin(tjeneste)
    except KeyboardInterrupt:
        print('\nStoppa av brukaren.')
    finally:
        pass

if __name__ == '__main__':
    main()
