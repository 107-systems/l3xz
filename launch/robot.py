from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    l3xz_io_dynamixel_launch_dir = get_package_share_directory('l3xz_io_dynamixel') + '/launch/io_dynamixel.py'
    l3xz_io_dynamixel = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_io_dynamixel_launch_dir))

    l3xz_head_ctrl_launch_dir = get_package_share_directory('l3xz_head_ctrl')  + '/launch/head_ctrl.py'
    l3xz_head_ctrl = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_head_ctrl_launch_dir))

    return LaunchDescription([
        l3xz_io_dynamixel,
        l3xz_head_ctrl
    ])
