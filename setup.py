from setuptools import setup, find_packages

setup(
    name='otsafe',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'pymodbus',
        'pyshark',
        'python-dotenv',
    ],
)