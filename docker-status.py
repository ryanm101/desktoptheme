#!/usr/bin/env python

from __future__ import print_function
import docker

client = docker.from_env()
for container in client.containers.list():
    print('{:40} {}'.format(container.attrs['Config']['Image'], container.status))
