import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.previous_x = 0.0
        self.cmd_vel_pub_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel', 10)    
        self.pose_subscriber_ = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback, 10)
        self.get_logger().info('Turtle Controller Node has started.')

    def pose_callback(self, Pose: Pose):
        cmd = Twist()
        if Pose.x > 9.0 or Pose.x < 2.0 or Pose.y > 9.0 or Pose.y < 2.0:
            cmd.linear.x = 1.0  
            cmd.angular.z = 0.9  
        else:
            cmd.linear.x = 5.0  
            cmd.angular.z = 0.0  
        self.cmd_vel_pub_.publish(cmd)  # Publish the velocity

        if Pose.x > 5.5 and self.previous_x <= 5.5:
            self.previous_x = Pose.x
            self.get_logger().info('Changing pen to RED')
            self.call_set_pen_servise(255, 0, 0, 3, 0)  
        elif Pose.x <= 5.5 and self.previous_x > 5.5:
            self.previous_x = Pose.x
            self.get_logger().info('Changing pen to GREEN')
            self.call_set_pen_servise(0, 255, 0, 3, 0)  


    def call_set_pen_servise(self, r, g, b, width, off):
        client = self.create_client(SetPen, '/turtle1/set_pen')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off
        future = client.call_async(request)

    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(
                'Service call failed %r' % (e,)) 

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()