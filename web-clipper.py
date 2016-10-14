#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Copyright (c) 2016, Antonio Coratelli.
Released under BSD 3-Clause License. See 'LICENSE' file.
'''

import os
import sys
import time
import requests
import subprocess
import argparse
import pypandoc
from urllib import urlencode
from pythonzenity import Entry as DialogAskString

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

    def __init__(self, pagefetcher):
        self.filename = None
        self.pagefetcher = pagefetcher

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
        editor_cl = editor.split(' ')
        subprocess.call(editor_cl + [filename_md], stdout=FNULL, stderr=FNULL)

    def get_filename(self):
        if self.filename is None:
            self.ask_filename()
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def ask_filename(self):
        default_filename = self.get_title()
        f = DialogAskString(title="web-clipper", text="Write filename without extension.", entry_text=default_filename)
        time.sleep(1)
        if f is None:
            f = default_filename
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
    ap.add_argument("-t", action="store_true", dest="title", default=False, help="use default file title")
    ap.add_argument("-A", action="store_true", dest="all", default=False, help="alias for '-e \"gedit -s\" -m -b'")

    args = ap.parse_args()

    if not args.editor is None:
        args.markdown = True
    if args.ebook is True:
        args.markdown = True
    if args.all is True:
        args.markdown = True
        args.ebook = True
        args.editor = "gedit -s"

    pf = PageFetcher(args.url)
    wc = WebClipper(pf)

    if args.title:
        title = wc.get_title()
        wc.set_filename(title)
    if args.markdown:
        print "Saving Markdown"
        wc.save_markdown()
    if not args.editor is None:
        print "Opening Editor"
        wc.open_editor(args.editor)
    if args.ebook:
        print "Saving Ebook"
        wc.save_ebook()
