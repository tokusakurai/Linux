#!/usr/bin/python3

import os

os.posix_spawn("/bin/echo", ["echo", "genereted by", "echo", "posix_spawn()"], {})
print("generated echo command")
