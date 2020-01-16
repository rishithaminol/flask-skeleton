#!/usr/bin/env bash

# git clone fomantic ui
# npm install
# Edit semantic.json file to ignore .css files and only keep min.css files
# Copy dist directory as assets/fomantic-ui



git clone https://github.com/fomantic/Fomantic-UI.git
cd Fomantic-UI

cat > semantic.json <<EOF
{
  "base": "",
  "paths": {
    "source": {
      "config": "src/theme.config",
      "definitions": "src/definitions/",
      "site": "src/site/",
      "themes": "src/themes/"
    },
    "output": {
      "packaged": "dist/",
      "uncompressed": "dist2/components/",
      "compressed": "dist/components/",
      "themes": "dist/themes/"
    },
    "clean": "dist/"
  },
  "permission": false,
  "autoInstall": false,
  "rtl": false,
  "version": "2.8.3"
}
EOF

rm -rf 'node_modules'
npm install
