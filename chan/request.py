#!/usr/bin/env python

import json
import urllib2
import socket

class InvalidRequest(Exception):
    def __str__(self):
        return 'Unable to handle given request'

def to_api(request):
    try:
        remote = urllib2.urlopen(request)
        return json.loads(remote.read())
    except (urllib2.HTTPError, socket.error):
        raise InvalidRequest()

def to_file(request):
    try:
        remote = urllib2.urlopen(request)
        return remote.read()
    except (urllib2.HTTPError, socket.error):
        raise InvalidRequest()

