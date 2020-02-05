#!/usr/bin/env bash

cd /home/centos/project-fp/
source ./venv/bin/activate

uwsgi --socket 127.0.0.1:5001 --processes 1 --threads 25 --chdir /home/centos/project-fp --mount /=server:app --uid 1000 --gid 1000