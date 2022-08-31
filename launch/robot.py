from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    l3xz_io = Node(
      package='l3xz_io',
      namespace='l3xz_io',
      executable='l3xz_io_node',
      name='l3xz_io',
      output='screen',
      parameters=[]
    )

    l3xz_head_ctrl = Node(
      package='l3xz_head_ctrl',
      namespace='l3xz',
      executable='l3xz_head_ctrl_node',
      name='l3xz_head_ctrl',
      output='screen',
      parameters=[]
    )

    l3xz_gait_ctrl = Node(
      package='l3xz_gait_ctrl',
      namespace='l3xz',
      executable='l3xz_gait_ctrl_node',
      name='l3xz_gait_ctrl',
      output='screen',
      parameters=[]
    )

    return LaunchDescription([
        l3xz_io,
        l3xz_head_ctrl,
        l3xz_gait_ctrl,
    ])
