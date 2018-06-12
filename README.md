# Jailbreak
Util for exporting directories from mono-repos to their own
repository.

Useful for open-sourcing a portion of your repository, and keeping
updates in sync.

## Installation
Clone this repo, then run `setup.sh`.

This script simply symlinks `jailbreak.py` to where you checked it out.

> **You should read `setup.sh` for yourself before running**

## Usage
In the directories you wish to push to a public repository, add a `.jailbreak` file, 
containing the git url of the open source repository you wish to publish to.

eg:

`foo/.jailbreak:`
```
git@github.com:hip-property/jailbreak.git
``` 

Then, from the root of your repository, run:

```bash
jailbreak foo
```
