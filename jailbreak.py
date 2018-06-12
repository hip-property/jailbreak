#!/usr/bin/env python3.6
import subprocess

remote = subprocess.run(["git", "remote", "-v"], universal_newlines=True)
print(remote.stdout)
