<a href="https://107-systems.org/"><img align="right" src="https://raw.githubusercontent.com/107-systems/.github/main/logo/107-systems.png" width="15%"></a>
L3X-Z
=====
[![Spell Check status](https://github.com/107-systems/l3xz/actions/workflows/spell-check.yml/badge.svg)](https://github.com/107-systems/l3xz/actions/workflows/spell-check.yml)

Home of L3X-Z, a mixed electric/hydraulic hexapod robot.

<p align="center">
  <a href="https://github.com/107-systems/l3xz"><img src="https://raw.githubusercontent.com/107-systems/l3xz_io/main/doc/img/2022-05-31-ELROB-2022-L3X-Z.jpg" width="40%"></a>
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
```bash
colcon_ws$ source install/setup.bash
colcon_ws$ ros2 launch l3xz control.py
```

#### Repositories
##### Host Software
* [l3xz_io](https://github.com/107-systems/l3xz_io): ROS based control software for L3X-Z, a mixed electric/hydraulic hexapod.
* [l3xz_joy](https://github.com/107-systems/l3xz_joy): ROS PS3 joystick driver for feeding `l3xz_teleop` node.
* [l3xz_teleop](https://github.com/107-systems/l3xz_teleop): Teleoperation for L3X-Z via PS3 joystick and ROS topics.
* [l3xz-mapping](https://github.com/107-systems/l3xz-mapping): Docker container containing the mapping stack for L3X-Z.
##### Robot Software
* [l3xz_sweep_scanner](https://github.com/107-systems/l3xz_sweep_scanner): ROS driver for Scanse Sweep 360° 2D LIDAR.
* [l3xz_openmv_camera](https://github.com/107-systems/l3xz_openmv_camera): ROS driver for OpenMV camera.
##### Hardware
* [l3xz-hw](https://github.com/107-systems/l3xz-hw): L3X-Z Hexapod hardware design files (3D model, printed parts, etc.).
* [l3xz-hw_leg-controller](https://github.com/107-systems/l3xz-hw_leg-controller): L3X-Z Hexapod leg controller hardware design files.
##### Firmware
* [l3xz-fw_aux-controller](https://github.com/107-systems/l3xz-fw_aux-controller): L3X-Z hexapod auxiliary controller firmware.
* [l3xz-fw_leg-controller](https://github.com/107-systems/l3xz-fw_leg-controller): L3X-Z hexapod leg controller firmware.
* [l3xz-fw_radiation_sensor](https://github.com/107-systems/l3xz-fw_radiation_sensor): L3X-Z hexapod firmware for the radiation sensor.
##### Dependencies
* [orocos-kdl](https://github.com/107-systems/orocos-kdl-debian): Prebuilt Debian package for `aarch64-linux-gnu` and `arm-linux-gnueabihf`.
