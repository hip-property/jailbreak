#!/usr/bin/env bash
chmod +x jailbreak.py
rm /usr/local/bin/jailbreak 2> /dev/null
ln -s $(pwd)/jailbreak.py /usr/local/bin/tino
