#!/bin/sh

val=$(rosparam get test_param)
echo "param = ${val}"
