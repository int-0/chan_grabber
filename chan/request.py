#!/usr/bin/env python

import json
import urllib.request
import socket

import chan.errors


def to_file(request):
    '''Send request and return response as data'''
    try:
        with urllib.request.urlopen(request) as response:
            return response.read()
    except Exception as error:
        raise chan.errors.InvalidRequest(str(error))


def to_api(request):
    '''Send request and parse response as JSON'''
    return json.loads(to_file(request))
