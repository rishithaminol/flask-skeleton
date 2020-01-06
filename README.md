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
