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
    
    l3xz_openmv_rgb = Node(
      package='l3xz_openmv_camera',
      executable='l3xz_openmv_camera',
      name='l3xz_openmv_rgb',
      namespace='l3xz',
      output='screen',
      parameters=[
          {'image_topic': 'image_rgb'},
          {'info_topic': 'info_rgb'},
          {'port': '/dev/serial/by-id/usb-OpenMV_OpenMV_Virtual_Comm_Port_in_FS_Mode_387C357D3330-if00'},
          {'frame_id': 'openmv_rgb_link'},
      ]
    )

   l3xz_openmv_thermal = Node(
      package='l3xz_openmv_camera',
      executable='l3xz_openmv_camera',
      name='l3xz_openmv_thermal',
      namespace='l3xz',
      output='screen',
      parameters=[
          {'image_topic': 'image_thermal'},
          {'info_topic': 'info_rgb'},
          {'port': '/dev/serial/by-id/usb-OpenMV_OpenMV_Virtual_Comm_Port_in_FS_Mode_3172326E3330-if00'},
          {'frame_id': 'openmv_thermal_link'},
      ]
    )
        
    return LaunchDescription([
        l3xz_io,
        l3xz_head_ctrl,
        l3xz_gait_ctrl,
        l3xz_openmv_rgb,
        l3xz_openmv_thermal
    ])
