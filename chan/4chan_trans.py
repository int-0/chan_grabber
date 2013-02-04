#!/usr/bin/env python

import translator

_API_URL = 'http://api.4chan.org/'
_FILE_BASE = 'http://images.4chan.org/'

class 4Chan_translator(tranlator.Translator):
    def __init__(self):
        translator.Translator.__init__(self)

    def thread(self, board_id, thread_id):
        if thread_id == 0:
            # Root thread
            return '%s%s/0.json' % (_API_URL,
                                    board_id)
        # Reply thread
        return '%s%s/res/%s.json' % (_API_URL,
                                     board_id,
                                     thread_id)

    def file(self, board_id, file_id):
        return '%s%s/src/%s%s' % (_FILE_BASE,
                                  board_id,
                                  file_id[0],
                                  file_id[1])
