#!/bin/bash

false &
wait $!
echo "finish false command: $?"
