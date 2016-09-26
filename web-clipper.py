#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from tkSimpleDialog import askstring as DialogAskString

class Readability:

    def get_token(self):
        pass

    def get_api_url(self, page_url):
        request = { 'url': page_url, 'token': self.get_token() }
        request_enc = ''
        return "http://readability.com/api/content/v1/parser?%s" % request_enc

    def fetch_page(url):
        pass

class WebClipper:

    def __init__(self, url):
        self.set_url(url)
        self.set_filename(None)

    def save_markdown(self):
        markdown = self.get_readable_markdown()
        filename = "%s.md" % self.get_filename()
        pass

    def save_ebook(self):
        markdown = self.get_readable_markdown()
        filename = "%s.ebook" % self.get_filename()
        pass

    def get_readable_markdown(self):
        pass

    def get_readable_html(self):
        pass

    def get_filename(self):
        if self.filename == None:
            self.ask_filename()
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def ask_filename(self):
        f = DialogAskString("web-clipper", "Write filename without extension.")
        self.set_filename(f)

    def open_editor(self):
        pass

    def fetch_page(self):
        pass

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url
