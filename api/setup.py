from setuptools import setup

# Just for 'pip install -e .'
# To make 'galpi' discoverable in tests
setup(
    name='galpi',
    packages=['galpi'],
    include_package_data=True,
)
