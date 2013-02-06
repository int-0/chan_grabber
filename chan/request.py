#!/usr/bin/env python

import json
import urllib2

def to_api(request):
    remote = urllib2.urlopen(request)
    return json.loads(remote.read())

def to_file(request):
    remote = urllib2.urlopen(request)
    return remote.read()
