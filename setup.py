from setup import setup, find_packages

setup(
    name='voodoo_tool',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'voodoo=main:main',
        ],
    },
    install_requires=[
        # List your dependencies here
    ],
    author='r3bus',
    description='Voodoo Tool - A cybersecurity toolkit',
    long_description=open('README.md').read(),
)


def setup():
    pass


def find_packages():
    pass