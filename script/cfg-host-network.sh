#!/bin/bash
sudo ifconfig eth0 down
sudo ifconfig eth0 192.168.88.3/24
sudo ifconfig eth0 up
