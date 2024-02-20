#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 <value>"
    exit 1
fi
export test="$1"
echo "Variable 'test' set to: $test"
exit 0