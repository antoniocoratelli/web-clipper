# web-clipper

> Easily download the main content of a web page in *html*, 
> *markdown*, and/or *epub* format from command line.

## Dependencies

This project was developed on *Ubuntu 14.04*, but *should* run smoothly on any Linux distribution
with `python3` and `virtualenv` support.

```
sudo apt-get -y install \
    git-core \
    python3 python3-pip python-virtualenv \
    python-tk openjdk-7-jdk libxml2-dev libxslt1-dev pandoc \
    && \
sudo apt-get -y build-dep \
    python-imaging \
    && \
pip3 install --user --upgrade \
    pip virtualenv
```

## Setup

```
git clone https://github.com/antoniocoratelli/web-clipper.git && cd web-clipper && ./init-venv.sh
```

## Usage

See script help: `./web-clipper -h`
