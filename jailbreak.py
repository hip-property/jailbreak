#!/usr/bin/env python3.6
import subprocess
import tempfile
import shutil
import argparse
import os
parser = argparse.ArgumentParser("Exports a single directory within the project to a seperate repository")
parser.add_argument("dir", help="The directory to be exported to a seperate repo", )
args = parser.parse_args()

destRepo = open("./" + args.dir + "/.jailbreak", "r").read()

# Find the current git remote
commandResult = subprocess.run(["git", "remote", "-v"], universal_newlines=True, stdout=subprocess.PIPE)
# origin  git@gitlab.com:hipproperty/jailbreak.git (fetch)
remotes = commandResult.stdout.splitlines()
#  git@gitlab.com:hipproperty/jailbreak.git
remoteUrl = remotes[0].split()[1]

print("We're gonna jailbreak '{}' to repo {}".format(args.dir, destRepo))
response = input("Press enter to confirm, or cancel to abort")

tempDir = tempfile.mkdtemp()

print("Cloning " + remoteUrl + " to " + tempDir)
subprocess.run(["git", "clone", remoteUrl, tempDir], universal_newlines=True, stdout=subprocess.PIPE)
os.chdir(tempDir)

print("Removing original origin remote")
subprocess.run(["git", "remote", "remove", "origin"])
print("Pruning")
subprocess.run(["git", "filter-branch", "--prune-empty", "--subdirectory-filter " + args.dir])
print("Adding upstream remote of " + remoteUrl)
subprocess.run(["git", "remote", "add", "origin", remoteUrl])

# ... do stuff with dirpath
# shutil.rmtree(dirpath)
