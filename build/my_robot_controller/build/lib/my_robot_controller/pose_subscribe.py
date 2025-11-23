import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__('pose_subscribe')
        self.pose_subscriber_ = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f'Turtle Pose - x: {msg.x}, y: {msg.y}, theta: {msg.theta}')

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()


    