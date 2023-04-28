#!/bin/bash
# Pavel Kirienko <pavel@uavcan.org>

HELP="Register slcan-enabled serial-to-CAN adapters as network interfaces.
Usage:
    `basename $0` [options] <tty0> [[options] <tty1> ...]

Interface indexes will be assigned automatically in ascending order, i.e., the
first device will be mapped to slcan0, second to slcan1, and so on.
Each added option affects only the interfaces that follow it,
which means that options must be properly ordered (see examples below).
This tool requires superuser privileges.

The package 'can-utils' must be installed. On Debian/Ubuntu-based systems it
can be installed via APT: apt-get install can-utils

Options:
  --speed-code <X> (where X is a number in range [0, 8]; default: 8)
  -s<X>
      Set CAN speed to:
      0 - 10  Kbps
      1 - 20  Kbps
      2 - 50  Kbps
      3 - 100 Kbps
      4 - 125 Kbps (UAVCAN recommended)
      5 - 250 Kbps (UAVCAN recommended)
      6 - 500 Kbps (UAVCAN recommended)
      7 - 800 Kbps
      8 - 1   Mbps (UAVCAN recommended, default)

  --remove-all
  -r
      Remove all SLCAN interfaces.
      If this option is used, it should be provided first, otherwise it
      will remove the interfaces added earlier.

  --basename <X> (where X is a string containing [a-z], default: slcan)
  -b<X>
      Base name to use for the interfaces that follow this option.

  --baudrate <X> (where X is an integer, default: 921600)
  -S<X>
      Configure baud rate to use on the interface.
      This option is mostly irrelevant for USB adapters.

  --silent
  -l
      Open the CAN interface in silent mode (listen-only, SLCAN command 'L\\r').

Example 1:
    `basename $0` --remove-all /dev/ttyUSB3 --basename can --baudrate 115200 \\
                     /dev/ttyUSB0 --speed-code 4 /dev/ttyACM0
The example above initializes the interfaces as follows:
    /dev/ttyUSB3  -->   slcan0     1 Mbps          baudrate 921600
    /dev/ttyUSB0  -->   can0       1 Mbps          baudrate 115200
    /dev/ttyACM0  -->   can1       125 kbps        baudrate 115200

Example 2:
    `basename $0` --remove-all
The example above only removes all SLCAN interfaces without adding new ones."

function die() { echo $@ >&2; exit 1; }

if [ "$1" == '--help' ] || [ "$1" == '-h' ]; then echo "$HELP"; exit; fi

[ -n "$1" ] || die "Invalid usage. Use --help to get help."

[ "$(id -u)" == "0" ] || die "Must be root."

which slcand > /dev/null || die "Please install can-utils first."

# ---------------------------------------------------------

function deinitialize() {
    echo "Stopping slcand..." >&2
    # Trying SIGINT first
    killall -INT slcand &> /dev/null
    sleep 0.3
    # Then trying the default signal, which is SIGTERM, if SIGINT didn't help
    slcand_kill_retries=10
    while killall slcand &> /dev/null
    do
        (( slcand_kill_retries -= 1 ))
        [[ "$slcand_kill_retries" > 0 ]] || die "Failed to stop slcand"
        sleep 1
    done
}

function handle_tty() {
    tty=$(readlink -f $1)
    iface_index=0
    while ip link show "$IFACE_BASENAME$iface_index" &> /dev/null
    do
        iface_index=$((iface_index + 1))
    done
    iface="$IFACE_BASENAME$iface_index"
    echo "Attaching '$tty' to '$iface' speed code '$SPEED_CODE' baudrate '$BAUDRATE' mode '$MODE'" >&2
    slcand -f -$MODE -s$SPEED_CODE $tty $iface || return 5
    sleep 1
    ip link set up $iface txqueuelen 500 || return 6
}

IFACE_BASENAME='slcan'
SPEED_CODE=8
BAUDRATE=921600
MODE='o'

next_option=''
while [ -n "$1" ]; do
    case $1 in
    -r | --remove-all)
        deinitialize
        ;;

    -b*)
        IFACE_BASENAME=${1:2}
        ;;

    -S*)
        BAUDRATE=${1:2}
        ;;

    -s[0-8])
        SPEED_CODE=${1:2}
        ;;

    -l | --silent)
        MODE='l'
        ;;

    --*)
        next_option=${1:2}
        ;;

    -*)
        die "Invalid option: $1"
        ;;

    *)
        if   [ "$next_option" = 'basename' ];   then IFACE_BASENAME=$1
        elif [ "$next_option" = 'speed-code' ]; then SPEED_CODE=$1
        elif [ "$next_option" = 'baudrate' ];   then BAUDRATE=$1
        elif [ "$next_option" = '' ]
        then
            handle_tty $1 || die "Failed to configure interface $1"
        else
            die "Invalid option '$next_option'"
        fi
        next_option=''
        ;;
    esac
    shift
done

[ "$next_option" = '' ] || die "Expected argument for option '$next_option'"
