https://flask.palletsprojects.com/en/1.1.x/tutorial/views/

Scripts directory
==================
Scripts in this directory should be used to manage the skeleton.
upgrade_assets.sh - This is the script which is used to upgrade all the assets (javascripts, css, semantic UI)
    This script must find it's base directory by using realpath.
    Then this script should find public assets directory
    Next Download required packages -> build -> deploy.
public - Publicly sharable documents (minified css and js. Images)
public-src - Source files which are later converted into minified css and js

Software upgrade with database deployment
===========================================
In order to keep current program live we have to keep some columns if we are going to remove them in the database updating stage.
Because current program will not work if we suddenly make database changes.
For errorless strategy we recommend first create a separate nullable column (If we are going to change colum name) and then develop your application using that column name ignoring previous name the column had.
Secondly copy none-existing data to the new column and quickly start new code.

Frontend static serving
=======================
In the frontend we map `/static` directory to `src/public`

How to run on production
========================
1. First create a virtual environment inside the directory using the command `virtualenv venv`.
2. Activate the environment using `. ./venv/bin/activate` and install the packages using `pip install -r requirements.txt`.
3. Run `alembic upgrade head` to update the database schema changes in the database.
4. `run.sh` is the main shell script responsible for running the application. In that script uwsgi program is running an application instance or instances inside the file `server.py` using the settings inside `uwsgi.ini`.
5. User ownerships in `uwsgi.ini` must be change accordingly in order to be easily communicate with `nginx` or `apache` web server.
6. `scripts/flask_skeleton.service` systemd unit file can be used to start the application on system reboots. All you have to do is change the configurations, path names and ownerships in that file.
7. Change the ownership of entire directory to the user specified in `uwsgi.ini` or `scripts/flask_skeleton.service`.
8. If `systemd` unit file rejects the execution of `uwsgi`, You can set all the `uwsgi` configurations inside that systemd unit file.
