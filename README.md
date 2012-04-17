Info about the project
======================

Web application for managing book collections

Quick start
===========

1. Download the sources: `git clone git@github.com:halish/ook.git`
2. (optional) Create Python virtual environment: `virtualenv --no-site-packages ook`. To activate: `source bin/activate`, to quit: `deactivate`.
3. Init buildout: `python bootstrap.py`
4. Download dependencies: `bin/buildout` (it downloads and compiles the node.js, so it may take few minutes).
5. Compile the CoffeeScript and less: `bin/cake`
6. Compile the Hogan templates: `bin/hulk ook/hogan/*.mustache > ook/media/js/templates.js`
7. Prepare the database: `django syncdb --migrate --noinput`
8. Run the server: `django runsever`
9. `http://localhost:8000/accounts/signin`
