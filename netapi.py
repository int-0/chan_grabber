#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python

import json
import urllib2
import common

def fetch(url):
    remote_object = urllib2.urlopen(url)
    return json.loads(remote_object.read())

def get_thumb(board_id, tim_code):
    thum_url = '%s%s/thumb/%ss.jpg' % (common.THM_URL,
                                       board_id,
                                       tim_code)
    remote_object = urllib2.urlopen(thumb_url)
    return remote_object.read()

def get_image(board_id, tim_code, extension):
    image_url = '%s%s/src/%s%s' % (common.IMG_URL,
                                   board_id,
                                   tim_code,
                                   extension)
    remote_object = urllib2.urlopen(image_url)
    return remote_object.read()
