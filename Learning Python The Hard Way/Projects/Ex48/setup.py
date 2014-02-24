try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Ex48",
    "author": "Joel Santiago",
    "url": "URL to get it at",
    "download_url": "Where to download it at",
    "author_email": "joel.santiago1@gmail.com",
    "version": "0.1",
    "install_requires": ['nose'],
    "packages": ["Ex48"],
    "scripts": [],
    "name": "Ex48"
}

setup(**config)
