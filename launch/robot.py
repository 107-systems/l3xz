from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ros2_dynamixel_bridge_launch_dir = get_package_share_directory('ros2_dynamixel_bridge') + '/launch/bridge-l3xz.py'
    ros2_dynamixel_bridge = IncludeLaunchDescription(PythonLaunchDescriptionSource(ros2_dynamixel_bridge_launch_dir))

    ros2_cyphal_bridge_launch_dir = get_package_share_directory('ros2_cyphal_bridge') + '/launch/bridge.py'
    ros2_cyphal_bridge = IncludeLaunchDescription(PythonLaunchDescriptionSource(ros2_cyphal_bridge_launch_dir))

    l3xz_pump_ctrl_launch_dir = get_package_share_directory('l3xz_pump_ctrl')  + '/launch/pump_ctrl.py'
    l3xz_pump_ctrl = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_pump_ctrl_launch_dir))

    l3xz_valve_ctrl_launch_dir = get_package_share_directory('l3xz_valve_ctrl')  + '/launch/valve_ctrl.py'
    l3xz_valve_ctrl = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_valve_ctrl_launch_dir))

    l3xz_system_monitor_launch_dir = get_package_share_directory('l3xz_system_monitor')  + '/launch/monitor.py'
    l3xz_system_monitor = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_system_monitor_launch_dir))

    l3xz_head_ctrl_launch_dir = get_package_share_directory('l3xz_head_ctrl')  + '/launch/head_ctrl.py'
    l3xz_head_ctrl = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_head_ctrl_launch_dir))

    l3xz_gait_ctrl_launch_dir = get_package_share_directory('l3xz_gait_ctrl')  + '/launch/gait_ctrl.py'
    l3xz_gait_ctrl = IncludeLaunchDescription(PythonLaunchDescriptionSource(l3xz_gait_ctrl_launch_dir))

    return LaunchDescription([
        ros2_dynamixel_bridge,
        ros2_cyphal_bridge,
        l3xz_pump_ctrl,
        l3xz_valve_ctrl,
        l3xz_system_monitor,
        l3xz_head_ctrl,
        l3xz_gait_ctrl
    ])
