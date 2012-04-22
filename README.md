Info about the project
======================

Web application for managing book collections

Quick start
===========

1. Download the sources: `git clone git@github.com:halish/ook.git`.
2. Create Python virtual environment: `virtualenv --no-site-packages ook; cd ook; source bin/activate;`
3. Init buildout: `pip zc.buildout`
4. Download dependencies: `bin/buildout` (it downloads and compiles the node.js and stuff, so it may take few minutes).
5. Compile the CoffeeScript and less: `bin/cake`.
6. Prepare the database: `django syncdb --migrate --noinput`. Fix the permissions with `django check_permissions`.
7. Run the server: `django runsever`.
8. `http://localhost:8000/accounts/signin/`.
