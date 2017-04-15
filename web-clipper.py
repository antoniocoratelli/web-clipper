#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (c) 2016, Antonio Coratelli.
Released under BSD 3-Clause License. See 'LICENSE' file.
'''

import argparse
import pypandoc
from newspaper import Article

class PageFetcher:

    def __init__(self, page_url):
        self.page_url = page_url
        self.extractor = Article(self.page_url)
        self.extractor.download()
        self.extractor.parse()

    def get_page_content(self):
        base = '''<h1>%s</h1><p><a href="%s">%s</a></p><p><img src="%s"/><p>%s</p>'''
        url = self.extractor.url
        ttl = self.extractor.title
        img = self.extractor.top_image
        txt = self.extractor.text
        return base % (ttl, url, url, img, txt.replace('\n\n', '</p><p>'))

class WebClipper:

    def __init__(self, pagefetcher, path):
        self.path = path
        self.pagefetcher = pagefetcher

    def save_html(self):
        with open("%s.html" % self.path, 'w') as f: f.write(self.get_content())

    def save_markdown(self):
        pypandoc.convert_text(self.get_content(), 'md', format='html', outputfile="%s.md" % self.path)

    def save_epub(self):
        pypandoc.convert_text(self.get_content(), 'epub', format='html', outputfile="%s.epub" % self.path)

    def get_content(self):
        return self.pagefetcher.get_page_content()

if __name__ == '__main__':

    ap = argparse.ArgumentParser(epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", action="store", type=str, metavar='URL',  help="url to be downloaded")
    ap.add_argument("out", action="store", type=str, metavar='PATH', help="path of the output files (no extension)")
    ap.add_argument("-H", action="store_true", dest="html",      default=False, help="save in html format")
    ap.add_argument("-M", action="store_true", dest="markdown",  default=False, help="save in markdown format")
    ap.add_argument("-E", action="store_true", dest="epub",      default=False, help="save in epub format")
    ap.add_argument("-A", action="store_true", dest="all",       default=False, help="save all formats")
    args = ap.parse_args()

    print('fetching page ...')
    pf = PageFetcher(args.url)
    wc = WebClipper(pf, args.out)

    if args.html     or args.all: print("saving html ...");     wc.save_html()
    if args.markdown or args.all: print("saving markdown ..."); wc.save_markdown()
    if args.epub     or args.all: print("saving epub ...");     wc.save_epub()
    print('done!')
