Info about the project
======================

Web application for managing book collections

Quick start
===========

1. Download the sources: `git clone git@github.com:halish/ook.git`.
2. Create Python virtual environment: `virtualenv --no-site-packages ook; cd ook; source bin/activate;`
3. Init buildout: `pip zc.buildout`
4. Download dependencies: `buildout`.
5. Compile the media `cake all`.
6. Prepare the database: `mkdir -p tmp/db/; django syncdb --migrate --noinput`.
7. Run the server: `django runsever`.
8. `http://localhost:8000/accounts/signin/`.
