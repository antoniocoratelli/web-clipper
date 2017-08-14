# web-clipper

Easily download the main content of a web page in *html*, *markdown*, and/or *epub* format from command line.

> This project is hosted on [GitLab][gl-link] and mirrored on [GitHub][gh-link].
> Please open *Issues* and *Merge Requests* on GitLab.

[gl-link]: https://gitlab.com/antoniocoratelli/web-clipper
[gh-link]: https://github.com/antoniocoratelli/web-clipper

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

## Support

If you like this application you can [share it][support_share], buy me a [coffe][support_paypal], or say thanks adding a [star][support_star].

[support_share]:  https://www.addtoany.com/share/#url=github.com/antoniocoratelli/web-clipper
[support_star]:   https://github.com/antoniocoratelli/web-clipper/stargazers
[support_paypal]: https://paypal.me/antoniocoratelli/3
