try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Ex47",
    "author": "Joel Santiago",
    "url": "URL to get it at",
    "download_url": "Where to download it at",
    "author_email": "joel.santiago1@gmail.com",
    "version": "0.1",
    "install_requires": ['nose'],
    "packages": ["Ex47"],
    "scripts": [],
    "name": "Ex47"
}

setup(**config)
