from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    l3xz_joy_launch_dir = get_package_share_directory('l3xz_joy') + '/launch/joy.py'
    l3xz_joy = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_joy_launch_dir))

    l3xz_teleop_launch_dir = get_package_share_directory('l3xz_teleop')  + '/launch/teleop.py'
    l3xz_teleop = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_teleop_launch_dir))

    return LaunchDescription([
        l3xz_joy,
        l3xz_teleop
    ])
