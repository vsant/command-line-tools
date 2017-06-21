#!/bin/bash

ONOFF=`networksetup -getairportpower en0 | awk '{ print $4; }'`
if [ $ONOFF = "On" ];then
  networksetup -setairportpower en0 off
else
  networksetup -setairportpower en0 on
fi
