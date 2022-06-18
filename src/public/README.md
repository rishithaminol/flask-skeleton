Fomantic UI build
=================
In order to build fommantic-ui you should put Fomantic-UI source directory on this `public` folder and configure `semantic.json` in root directory and configure `src/theme.config` configuration.

Install `gulp` globally and run `gulp build` or `gulp watch` to periodically watch and build your changes.

`semantic.json` file
====================
  {
    "base": "",

    "paths": {
      "source": {
        "config"      : "src/theme.config",
        "definitions" : "src/definitions/",
        "site"        : "src/site/",
        "themes"      : "src/themes/"
      },
      "output": {
        "packaged"     : "../fomantic-ui/",
        "uncompressed" : "../fomantic-ui/components/",
        "compressed"   : "../fomantic-ui/components/",
        "themes"       : "../fomantic-ui/themes/"
      },
      "clean"        : "../fomantic-ui/"
    },

    "permission" : false,
    "autoInstall": false,
    "rtl": false
  }

Configure as per your need.
