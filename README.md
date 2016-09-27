# web-clipper

Download a web page in Markdown and/or Epub format.

## Usage

```
usage: web-clipper.py [-h] [-m] [-b] [-e EDITOR] URL

positional arguments:
  URL         url to be downloaded

optional arguments:
  -h, --help  show this help message and exit
  -m          save in markdown format
  -b          save in ebook format (implies '-m')
  -e EDITOR   open markdown file in editor (implies '-m', and it's done before
              converting the page in ebook format)

Copyright (c) 2016, Antonio Coratelli.
Released under BSD 3-Clause License. See 'LICENSE' file.
```

## Requirements

This indicator requires the following python modules: `os`, `sys`, `requests`,
`subprocess`, `argparse`, `pypandoc`, `urllib`, `Tkinter`.
You can install the missing ones using `pip` ([link][pip]).

## Acknowledgements

The script uses [FuckYeahMarkdown! API][fym] by Brett Terpstra.

## Support

If you like this application, you can [share it][support_share],
[buy me a coffe][support_paypal], or just say thanks adding a
[star][support_star] :)


[fym]: http://fuckyeahmarkdown.com/
[pip]: https://wiki.python.org/moin/CheeseShopTutorial#Installing_Distributions

[support_share]:  https://www.addtoany.com/share/#url=github.com/antoniocoratelli/web-clipper
[support_star]:   https://github.com/antoniocoratelli/web-clipper/stargazers
[support_paypal]: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RTG5FHAJKSYYN
