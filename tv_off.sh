#!/bin/bash
#echo "standby 0.0.0.0" | cec-client -s -d 1
cec-ctl -d/dev/cec0 --to 0 --standby
