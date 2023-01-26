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
##### Firmware
* [l3xz-aux-ctrl-firmware](https://github.com/107-systems/l3xz-aux-ctrl-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) auxiliary controller ([OpenCyphalPicoBase](https://github.com/generationmake/OpenCyphalPicoBase)).
* [l3xz-leg-ctrl-firmware](https://github.com/107-systems/l3xz-leg-ctrl-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) leg controller ([l3xz-leg-ctrl-hardware](https://github.com/107-systems/l3xz-leg-ctrl-hardware)).
* [l3xz-radiation-sensor-firmware](https://github.com/107-systems/l3xz-radiation-sensor-firmware): Firmware for the [L3X-Z](https://github.com/107-systems/l3xz) radiation sensor ([OpenCyphalPicoBase](https://github.com/generationmake/OpenCyphalPicoBase)).
##### Hardware
* [l3xz-leg-ctrl-hardware](https://github.com/107-systems/l3xz-leg-ctrl-hardware): L3X-Z Hexapod leg controller hardware design files.
* [l3xz-hw-rs485-power-injector](https://github.com/107-systems/l3xz-hw-rs485-power-injector): Provide battery power to RS485 devices.
* [CAN-Power-Injector](https://github.com/107-systems/CAN-Power-Injector): Provide power via CAN to all L3X-Z CAN devices.
##### CAD
* [l3xz-cad](https://github.com/107-systems/l3xz-cad): L3X-Z Hexapod hardware design files (3D model, printed parts, etc.).
* [l3xz-hw-pan-tilt-head](https://github.com/107-systems/l3xz-hw-pan-tilt-head): Design files for L3X-Zs pan/tilt color/thermal camera head.
##### Dependencies
* [libdynamixelplusplus](https://github.com/107-systems/libdynamixelplusplus): C++17 wrapper for the Robotis Dynamixel servo protocol.
* [orocos-kdl](https://github.com/107-systems/orocos-kdl-debian): Prebuilt Debian package for `aarch64-linux-gnu` and `arm-linux-gnueabihf`.

### Configuration
#### Network Configuration
| Component | IP | Notes |
|-|:-:|-|
| MikroTik "Base Station" | 192.168.88.2 (Bridge-IP) | (station bridge, nv2, pre-shared-key, l...) |
| MikroTik "Robot" | 192.168.88.1 (Bridge-IP) | (bridge, nv2, pre-shared-key, l...) |
| Robot Rasperry Pi (Ethernet) | 192.168.88.5 | |
| Control PC (Ethernet) | 192.168.88.3 | |

#### Cyphal Configuration
| Cyphal Node | ID |
|-|:-:|
| [Leg Controller](https://github.com/107-systems/l3xz-leg-ctrl-firmware) | 1-6 |
| [Auxiliary Controller](https://github.com/107-systems/l3xz-aux-ctrl-firmware) | 20 |
| [Radiation Sensor](https://github.com/107-systems/l3xz-radiation-sensor-firmware) | 21 |
| [Zubax Robotics Orel 20](https://files.zubax.com/products/io.px4.sapog/Zubax_Orel_20_Datasheet.pdf) | 10 |


### Components
#### Actuators
- 6 x [Dynamixel MX-28AR](https://emanual.robotis.com/docs/en/dxl/mx/mx-28-2/) servo (RS485, for hip (coxa) rotation)
- 12 x [Leimbach 0H1650A Hydraulic Zylinder](http://leimbach-modellbau.de/Produkte/Hydraulik/Zylinder/0H16xxxA/) (femur and tibia)
- 1 x [Lynxmotion SSC-32](http://www.lynxmotion.com/p-1032-ssc-32u-usb-servo-controller.aspx): servo controller for hydraulic valves.
- 12 x [Leimbach 0H1650A Hydraulic Zylinder](http://leimbach-modellbau.de/Produkte/Hydraulik/Zylinder/0H16xxxA/) (femur and tibia)
- 2 x [Leimbach 0H506A Standard Hydraulik-Ventile 6-fach](http://leimbach-modellbau.de/Produkte/Hydraulik/Ventile/0H50x/) 
- 12 x [Leimbach 0H518F Servo FUTABA s3107 ( für Steuerventil )](http://leimbach-modellbau.de/Produkte/Elektronik/0H518F/) 
- 1 x [Leimbach 0H108A Doppelpumpeneinheit M4](http://leimbach-modellbau.de/Produkte/Hydraulik/Pumpen/0H108(A)/) 

#### Sensors
  - 1 x [OpenMV Cam H7 R2](https://openmv.io/collections/cams/products/openmv-cam-h7-r2): Vision
  - 1 x [OpenMV Cam H7 R2](https://openmv.io/collections/cams/products/openmv-cam-h7-r2) + [FLIR Lepton Adapter Module](https://openmv.io/collections/cams/products/flir-lepton-adapter-module) + [FLIR Lepton](https://store.groupgets.com/products/flir-lepton-3-5): Thermal Vision
  - 1 x [Scanse Sweep](https://github.com/scanse/sweep-sdk): 360 ° LIDAR (SLAM/Mapping)
  - 12 x [AS5048A](https://ams.com/en/as5048a): 14-Bit rotary angle sensor for detecting position of femur/tibia
  - radiation sensor
  - 6 x [LAS4GQH-11/S](https://www.conrad.de/de/p/tru-components-las4gqh-11-s-drucktaster-220-v-dc-0-50-a-1-x-aus-ein-tastend-1-st-1661900.html): mechanical bumper switch at the foot endpoint to determine if the leg has ground contact
  - 1 x [Zubax Babel](https://zubax.com/products/babel): USB to CAN adapter, for UAVCAN communication
  - 1 x [Intel Realsense](https://www.intelrealsense.com/depth-camera-d435i) D435i

#### Networking
  - 2 x MikroTik [RBMetal5SHPn](https://mikrotik.com/product/RBMetal5SHPn)
