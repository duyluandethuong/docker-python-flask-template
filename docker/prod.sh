#!/bin/bash

_dockerDir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

exec docker-compose -p raspi-frame \
  -f "$_dockerDir/compose.yml" \
  -f "$_dockerDir/compose.prod.yml" \
  "$@"
