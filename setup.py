from setuptools import setup, find_packages

setup(
    name='otsafe',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'pymodbus',
        'pyshark',
        'python-dotenv',
    ],
)