#!/bin/bash


if [ "$1" == "-h" ]; then
  echo "Deploy tool: jeno"
  echo "Usage: ./jeno.sh counter || gify"
  echo "** Default: Deploying gify-panda AND counter-panda **"
  echo "Example: ./jeno.sh counter"
  echo "Example2: ./jeno.sh " 
  exit 0
fi

if ! [ ! $1 ]; then
  if ! { [ "$1" == "gify" ] || [ "$1" == "counter" ]; }; then
    echo "Please use './jeno.sh' -h for more help"
    exit 0
  fi
fi

[[ ! $1 ]] && TAG="counter-panda, gify-panda" || TAG="$1-panda"
echo "START Deploying: $TAG to Base container"
ansible-playbook base.yml --tags "$TAG"


