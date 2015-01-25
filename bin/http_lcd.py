#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""
:References:
    `coverage <../../../cover/bin_http_lcd.html>`_

Implement a HD44780 LCD in HTML.
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import logger
LOG = logger.Log(__file__)

try:
    #pylint: disable=F0401
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

import mmap

SCREEN = None

class LCDHTTPRequestHandler(BaseHTTPRequestHandler):
    """Provide a HTTP interface to the LCD"""
    
    #pylint: disable=C0103
    def do_GET(self):
        """Return the cuttent LCD data as HTML"""
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=UTF-8")
        self.send_header("Refresh", "1; url=#")
        self.end_headers()
        SCREEN.seek(0)
        buf = SCREEN.read(32)
        self.wfile.write(bytes("""<!DOCTYPE html>
<html>
<title>Doorbot</title>
<style>
td {
    margin:0px;
    padding:5px 2px 5px 2px;
    width:1em;
    text-align:center;
    font-family: digital, courier;
    font-weight: bold;
    color: red;
    background-color: black;
}
</style>
<body>
<table>
<tr>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<tr>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
<td>%s</td>
""" % tuple([i for i in buf])))

def main():
    """Start the HTTP deamon"""
    #pylint: disable=W0603
    global SCREEN
    with open('screen.dat', "rb+") as screenfile:
        SCREEN = mmap.mmap(screenfile.fileno(), 0)
    httpd = HTTPServer(('', 8000), LCDHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()

