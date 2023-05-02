#!/bin/bash
if [[ ! -v CYPHAL_PATH ]]; then
    echo "CYPHAL_PATH is not set"
elif [[ -z "$CYPHAL_PATH" ]]; then
    echo "CYPHAL_PATH is set to the empty string"
else
    echo "CYPHAL_PATH has the value: $CYPHAL_PATH"
fi
export UAVCAN__CAN__IFACE='socketcan:can0'
export UAVCAN__CAN__MTU=8
export UAVCAN__NODE__ID=$(yakut accommodate)  # Pick an unoccupied node-ID automatically for this shell session.
echo "Auto-selected node-ID for this session: $UAVCAN__NODE__ID"
