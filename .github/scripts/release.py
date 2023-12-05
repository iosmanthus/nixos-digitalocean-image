#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.PyGithub -I nixpkgs=https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz

import os

from github import Github
from datetime import datetime

g = Github(os.getenv('GITHUB_TOKEN'))
repo_name = os.getenv('GITHUB_REPOSITORY')
ref = os.getenv('GITHUB_SHA')
repo = g.get_repo(repo_name)
image_filename = 'nixos.qcow2.gz'
tag = datetime.now().strftime('%Y%m%d%H%M%S')

release = repo.create_git_release(tag=tag,
                                  name=tag,
                                  message=f'qcow2 image built from {ref}',
                                  target_commitish=ref,
                                  draft=False,
                                  prerelease=False)
release.upload_asset(f'./result/{image_filename}', name=image_filename)