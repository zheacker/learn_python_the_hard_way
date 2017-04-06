try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Zac Heacker',
    'url': 'url to get it at (github)',
    'download_url': 'where to download it (github)',
    'author_email': 'zac.heacker@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectName'
}

setup(**config)
