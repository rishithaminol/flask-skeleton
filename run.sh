#!/usr/bin/env bash

basedir=$(dirname $(realpath $0))
cd "$basedir"
source ./venv/bin/activate

uwsgi --ini uwsgi.ini
