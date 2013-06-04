PhotoViewerExpress README
==================

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/initialize_PhotoViewerExpress_db development.ini

- $venv/bin/pserve development.ini

## PIL Dependences
apt-get install libjpeg-dev zlib1g-dev
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib
