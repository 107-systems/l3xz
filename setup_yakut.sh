#!/bin/bash
if [[ ! -v CYPHAL_PATH ]]; then
    echo "CYPHAL_PATH is not set." >> /dev/stderr
    exit 1
elif [[ -z "$CYPHAL_PATH" ]]; then
    echo "CYPHAL_PATH is set to the empty string." >> /dev/stderr
    exit 1
else
    echo "CYPHAL_PATH = \"$CYPHAL_PATH\""
fi

if ! [ -e /sys/class/net/can0 ]; then
    sudo ./setup_slcan.sh --remove-all --basename can --speed-code 5 /dev/serial/by-id/usb-Zubax*Babel*
fi
export UAVCAN__CAN__IFACE='socketcan:can0'

export UAVCAN__CAN__MTU=8
export UAVCAN__NODE__ID=$(yakut accommodate)  # Pick an unoccupied node-ID automatically for this shell session.
echo "Auto-selected node-ID for this session: $UAVCAN__NODE__ID"
