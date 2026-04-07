import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from builtin_interfaces.msg import Time

from math import sin

class JointStatePublisher(Node):


    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(
            0.1, self.publish_joint_states)  # Publish every 0.1s
        
        # --- Inicialización de variables de estado ---
        self.t = 0.0
        self.s = True

    def publish_joint_states(self):
        
        if self.s == True:
            if self.t < 2:
                self.t += 0.01
            else:
                self.s = False
                
        else:
            if self.t > -2:
                self.t -= 0.01
            else:
                self.s = True

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()  # Add timestamp
        msg.name = [
            'q1', 'q2', 'q3'
        ]
        msg.position = [sin(self.t), sin(self.t), sin(self.t)]

        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published Joint States: {msg.position}')  # Debugging info


def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from pynput import keyboard

class TeleopJoints(Node):
    def __init__(self):
        super().__init__('teleop_joints')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.05, self.publish_joint_states)
        
        self.t = 0.0
        
        # Listener de teclado no bloqueante
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.t += 0.05
            elif key.char == 's':
                self.t -= 0.05
        except AttributeError:
            pass

    def on_release(self, key):
        self.velocidad = 0.0  # Se detiene al soltar la tecla
        if key == keyboard.Key.esc:
            return False # Detener listener

    def publish_joint_states(self):
        
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['q1', 'q2', 'q3']
        msg.position = [self.t, self.t, self.t]
        
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = TeleopJoints()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

"""