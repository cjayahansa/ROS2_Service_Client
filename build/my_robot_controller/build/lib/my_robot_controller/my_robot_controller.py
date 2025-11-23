import rclpy
from rclpy.node import Node
class MYNode(Node):
    def __init__(self):
        super().__init__('my_robot_controller')
        self.create_timer(1.0, self.timer_callback)
        self.counter_=0

    def timer_callback(self):
        self.get_logger().info('My Robot Controller is running...'+str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = MYNode()
    rclpy.spin(node)
    #meken thami loop ekk wage wada karnne
 
    rclpy.shutdown()
if __name__ == '__main__':
    main()