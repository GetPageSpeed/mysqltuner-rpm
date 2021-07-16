#!/usr/bin/env python3
# fetch latest release number for each OS and populate "releases" key in matrix.yml
# with current and previous release numbers (building for last two major)
import lastversion
import yaml
# fetch matrix.yml from GetPageSpeed?
import os

abspath = os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))
with open("matrix.yml", 'r') as f:
    try:
        distros_config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)

distros = distros_config['distros']
for distro in distros:
    distro_version = lastversion.latest(distro).release[0]
    print(f"{distro}'s latest major version is {distro_version}")
    distros[distro]['versions'] = [
        distro_version - 1,
        distro_version
    ]
print(distros)

# build up final yml based on header.yml and set up jobs: and workflows:
config = {
    'version': '2.1',
    'jobs': {},
    'workflows': {'all': {'jobs': ['el6']}}}

with open('header.yml') as f:
    header_config = yaml.safe_load(f)
    print(header_config)


for distro in distros:
    print(distro)
    for v in distros[distro]['versions']:
        distro_build_job = header_config['defaults']
        distro_build_job['docker'] = [
            { 'image': 'getpagespeed/rpmbuilder:centos-6' }
        ]
        config['jobs']['el6'] = distro_build_job

with open('generated_config.yml', 'w') as f:
    yaml.dump(config, f, default_flow_style=None)