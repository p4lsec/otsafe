FROM ubuntu:22.04 AS base

RUN apt-get update

# Application Dependencies
RUN DEBIAN_FRONTEND=noninteractive apt install -y  \
    python3-pip

RUN mkdir -p $HOME/output && \
    chmod og+rw $HOME/output && \
    mkdir -p $HOME/result && mkdir -p $HOME/files

# Copy files
COPY . .
RUN pip3 install -r $HOME/requirements.txt
RUN python3 $HOME/setup.py install

ENTRYPOINT ["python3", "app.py"]