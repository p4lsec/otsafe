# Install

To install the core library from PyPI:

```
pip install otsafe
```

To clone the repo in order to install the full suite, Jenkins, etc:

```
git clone git@github.com:p4lsec/otsafe.git
cd otsafe
pip install .
```

# Jenkins

In order to use the CI/CD pipeline features, you will need it:

- Modify docker-copose.yml to include DB creds
- run `docker-compose up`
- Monitor the output for a password logged to stdout
- Navigate to `127.0.0.1:80`
- When prompted, paste the password, then reset.