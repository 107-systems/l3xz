<a href="https://107-systems.org/"><img align="right" src="https://raw.githubusercontent.com/107-systems/.github/main/logo/107-systems.png" width="15%"></a>
L3X-Z
=====
[![Spell Check status](https://github.com/107-systems/l3xz/actions/workflows/spell-check.yml/badge.svg)](https://github.com/107-systems/l3xz/actions/workflows/spell-check.yml)

Home of L3X-Z, a mixed electric/hydraulic hexapod robot.

<p align="center">
  <a href="https://github.com/107-systems/l3xz"><img src="https://raw.githubusercontent.com/107-systems/.github/main/logo/l3xz-logo-memento-mori-github.png" width="40%"></a>
</p>

#### Video

<p align="center">
  <a href="https://107-systems.org/elrob-2022/2022-05-31-ELROB-2022-Alex-02-compressed.mp4"><img src="2022-05-31-ELROB-2022-L3X-Z.jpg" width="40%"></a>
</p>

#### Articles
* A. Entinger (2022, June 8). [L3X-Z - A OpenCyphal enabled hexapod robot for ELROB 2022](https://forum.opencyphal.org/t/l3x-z-a-opencyphal-enabled-hexapod-robot-for-elrob-2022/).
* R. Kim (2022, June 17). [LXRobotics - L3XZ Hexapod Robot for ELROB 2022](https://community.robotis.us/t/lxrobotics-l3xz-hexapod-robot-for-elrob-2022).

#### How-to-build
```bash
colcon_ws/src$ git clone https://github.com/107-systems/l3xz
colcon_ws$ source /opt/ros/galactic/setup.bash
colcon_ws$ colcon build --packages-select l3xz
```

#### How-to-run
**L3X-Z Hexapod Robot**
```bash
colcon_ws$ source install/setup.bash
colcon_ws$ ros2 launch l3xz robot.py
```

**Control Station**
```bash
colcon_ws$ source install/setup.bash
colcon_ws$ ros2 launch l3xz control.py
```

#### Repositories
##### Host Software
* [l3xz_joy](https://github.com/107-systems/l3xz_joy): ROS PS3 joystick driver for feeding `l3xz_teleop` node.
* [l3xz_teleop](https://github.com/107-systems/l3xz_teleop): Teleoperation for L3X-Z via PS3 joystick and ROS topics.
* [l3xz_mapping](https://github.com/107-systems/l3xz_mapping): L3X-Z mapping stack.
* [l3xz_frontend](https://github.com/107-systems/l3xz_frontend): Web based frontend for L3X-Z.
##### Robot Software
* [l3xz_io](https://github.com/107-systems/l3xz_io): ROS based control software for L3X-Z, a mixed electric/hydraulic hexapod.
* [l3xz_gait_ctrl](https://github.com/107-systems/l3xz_gait_ctrl): Gait controller for the L3X-Z electric/hydraulic hexapod robot.
* [l3xz_head_ctrl](https://github.com/107-systems/l3xz_head_ctrl): Head controller for the L3X-Z electric/hydraulic hexapod robot.
* [l3xz_sweep_scanner](https://github.com/107-systems/l3xz_sweep_scanner): ROS driver for Scanse Sweep 360° 2D LIDAR.
* [l3xz_openmv_camera](https://github.com/107-systems/l3xz_openmv_camera): ROS driver for OpenMV camera.
##### Hardware
* [l3xz-hw](https://github.com/107-systems/l3xz-hw): L3X-Z Hexapod hardware design files (3D model, printed parts, etc.).
* [l3xz-leg-ctrl-hardware](https://github.com/107-systems/l3xz-leg-ctrl-hardware): L3X-Z Hexapod leg controller hardware design files.
* [l3xz-hw_power_distribution_block](https://github.com/107-systems/l3xz-hw_power_distribution_block): Power distribution block for the L3X-Z hexapod robot.
* [l3xz-hw-rs485-power-injector](https://github.com/107-systems/l3xz-hw-rs485-power-injector): Provide battery power to RS485 devices.
* [l3xz-hw-pan-tilt-head](https://github.com/107-systems/l3xz-hw-pan-tilt-head): Design files for L3X-Zs pan/tilt color/thermal camera head.
* [CAN-Power-Injector](https://github.com/107-systems/CAN-Power-Injector): Provide power via CAN to all L3X-Z CAN devices.

##### Firmware
* [l3xz-aux-ctrl-firmware](https://github.com/107-systems/l3xz-aux-ctrl-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) auxiliary controller ([OpenCyphalPicoBase](https://github.com/generationmake/OpenCyphalPicoBase)).
* [l3xz-leg-ctrl-firmware](https://github.com/107-systems/l3xz-leg-ctrl-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) leg controller ([l3xz-leg-ctrl-hardware](https://github.com/107-systems/l3xz-leg-ctrl-hardware)).
* [l3xz-radiation-sensor-firmware](https://github.com/107-systems/l3xz-radiation-sensor-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) radiation sensor ([OpenCyphalPicoBase](https://github.com/generationmake/OpenCyphalPicoBase)).
##### Dependencies
* [libdynamixelplusplus](https://github.com/107-systems/libdynamixelplusplus): C++17 wrapper for the Robotis Dynamixel servo protocol.
* [orocos-kdl](https://github.com/107-systems/orocos-kdl-debian): Prebuilt Debian package for `aarch64-linux-gnu` and `arm-linux-gnueabihf`.
