#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Copyright (c) 2016, Antonio Coratelli.
Released under BSD 3-Clause License. See 'LICENSE' file.
'''

import os
import sys
import requests
import subprocess
import argparse
import pypandoc
from urllib import urlencode
import Tkinter as tk
from tkSimpleDialog import askstring as DialogAskString

class PageFetcher:

    def __init__(self, page_url):
        self.api_response = None
        self.page_url = page_url

    def get_page_content(self):
        r = self.get_api_response()
        markdown = r['markdown'].encode('utf-8', 'ignore')
        content = "# %s\n\n> %s\n\n%s" % (
            self.get_page_title(),
            self.page_url,
            markdown)
        return content

    def get_page_title(self):
        r = self.get_api_response()
        return r['title'].encode('utf-8', 'ignore')

    def get_api_response(self):
        if self.api_response is None:
            requests.adapters.DEFAULT_RETRIES = 10
            r = requests.get(self.get_api_url())
            r.raise_for_status()
            self.api_response = r.json()
        return self.api_response

    def get_api_url(self):
        request_dict = { 'u': self.page_url, 'output': 'json', 'md': '1' }
        request = urlencode(request_dict)
        return "http://fuckyeahmarkdown.com/go/?%s" % request


class WebClipper:

    def __init__(self, url):
        self.filename = None
        self.url = url
        self.pagefetcher = PageFetcher(self.url)

    def save_markdown(self):
        markdown = self.get_content()
        filename_md = "%s.md" % self.get_filename()
        with open(filename_md, 'w') as f:
            f.write(markdown)
        return filename_md

    def save_ebook(self):
        filename_md = "%s.md" % self.get_filename()
        filename_epub = "%s.epub" % self.get_filename()
        pypandoc.convert_file(filename_md, 'epub', outputfile=filename_epub)
        return filename_epub

    def open_editor(self, editor):
        filename_md = self.save_markdown()
        FNULL = open(os.devnull, 'w')
        subprocess.call([editor, filename_md], stdout=FNULL, stderr=FNULL)

    def get_filename(self):
        if self.filename is None:
            self.ask_filename()
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def ask_filename(self):
        root = tk.Tk()
        root.withdraw()
        default = self.get_title()
        f = DialogAskString("web-clipper", "Write filename without extension.", initialvalue=default)
        self.set_filename(f)

    def get_content(self):
        return self.pagefetcher.get_page_content()

    def get_title(self):
        return self.pagefetcher.get_page_title()


if __name__ == '__main__':

    ap = argparse.ArgumentParser(epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", action="store", type=str, metavar='URL', help="url to be downloaded")
    ap.add_argument("-m", action="store_true", dest="markdown", default=False, help="save in markdown format")
    ap.add_argument("-b", action="store_true", dest="ebook", default=False, help="save in ebook format (implies '-m')")
    ap.add_argument("-e", action="store", dest="editor", default=None, help="open markdown file in editor (implies '-m', and it's done before converting the page in ebook format)")

    args = ap.parse_args()

    if not args.editor is None: args.markdown = True
    if args.ebook is True: args.markdown = True

    wc = WebClipper(args.url)
    if args.markdown: wc.save_markdown()
    if not args.editor is None: wc.open_editor(args.editor)
    if args.ebook: wc.save_ebook()
