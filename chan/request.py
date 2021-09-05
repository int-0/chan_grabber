#!/usr/bin/env python

import json
import urllib.request
import socket

class InvalidRequest(Exception):
    def __str__(self):
        return 'Unable to handle given request'

def to_api(request):
    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read())
    except (Exception):
        raise InvalidRequest()

def to_file(request):
    try:
        with urllib.request.urlopen(request) as response:
            return response.read()
    except (Exception):
        raise InvalidRequest()
