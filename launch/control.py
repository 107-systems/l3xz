from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory

import os

def generate_launch_description():
    l3xz_joy = Node(
      package='l3xz_joy',
      executable='l3xz_joy_node',
      name='joy',
      namespace='l3xz',
      output='screen',
      parameters=[
        {'joy_dev_node': '/dev/input/js0'},
        {'joy_topic': 'joy'},
        {'joy_topic_publish_period_ms': 50},
        { 'joy_deadzone': 0.01 },
      ]
    )

    l3xz_teleop = Node(
      package='l3xz_teleop',
      executable='l3xz_teleop_node',
      name='teleop_node',
      namespace='l3xz',
      output='screen',
      parameters=[
          {'joy_topic': 'joy'},
          {'robot_topic': 'cmd_vel_robot'},
          {'head_topic': 'cmd_vel_head'},
      ]
    )

    return LaunchDescription([
        l3xz_joy,
        l3xz_teleop,
    ])
