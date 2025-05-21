from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='test1',
            executable='test1_node',
            name='test1_node',
            output='screen'
        )
    ])