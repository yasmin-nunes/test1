#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class TestNode(Node):
    def __init__(self):
        super().__init__('test1_node')
        self.get_logger().info('Nó iniciado com sucesso!')
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Publicando mensagem a cada 2 segundos...')

def main(args=None):
    rclpy.init(args=args)
    node = TestNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()