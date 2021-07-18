from setuptools import setup
setup(
    name = 'pycli',
    version = '1.0.0',
    packages = ['blogcli'],
    entry_points = {
        'console_scripts': [
            'blogcli = blogcli.__main__:main'
        ]
    })

# run:  sh install.sh
# USAGE: blogcli
# Enter the requested details -> need to try and read from a file!
