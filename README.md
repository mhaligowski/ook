Info about the project
======================

Web application for managing book collections

Quick start
===========

1. Download the sources: `git clone git@github.com:halish/ook.git`
2. Create Python virtual environment: `virtualenv --no-site-packages ook; cd ook; source bin/activate;`
3. Init buildout: `pip zc.buildout`
4. Download dependencies: `buildout` (it downloads and compiles the node.js, so it may take few minutes).
5. Compile the CoffeeScript and less: `cake`
6. Compile the Hogan templates: `bin/hulk ook/hogan/*.mustache > ook/media/js/templates.js`
7. Prepare the database: `django syncdb`
8. Run the migrations: `django migrate`
9. Run the server: `django runsever`
10. `http://localhost:8000/accounts/signin`
