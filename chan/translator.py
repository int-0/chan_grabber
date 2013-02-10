#!/usr/bin/env python

# A Translator() object converts thread-ids and file-ids
# into HTTP requests
#

MAX_PAGES = 50

class InvalidThread(Exception):
    def __init__(self, id):
        self.__id = id
    def __str__(self):
        return 'Unknown thread #id %s' % self.__id

class InvalidFile(Exception):
    def __init__(self, id):
        self.__id = id
    def __str__(self):
        return 'Unknown file #id %s' % self.__id

# Generic translator interface
class Translator(object):
    def __init__(self, board_id):
        self.__board_id = board_id

    @property
    def max_pages(self):
        return MAX_PAGES

    @property
    def board_id(self):
        return self.__board_id

    def thread(self, thread_id):
        raise NotImplementedError()

    def file(self, file_id):
        raise NotImplementedError()

    def thumb(self, file_id):
        raise NotImplementedError()

# Translator for 4CHAN
class T4Chan(Translator):
    def __init__(self, board_id):
        Translator.__init__(self, board_id)
        self._API_URL = 'http://api.4chan.org/'
        self._FILE_BASE = 'http://images.4chan.org/'
        self._THUMB_BASE = 'http://thumbs,4chan.org/'

    def thread(self, thread_id):
        if thread_id < self.max_pages:
            # Root thread
            return '%s%s/%s.json' % (self._API_URL,
                                     self.board_id,
                                     thread_id)
        # Reply thread
        return '%s%s/res/%s.json' % (self._API_URL,
                                     self.board_id,
                                     thread_id)

    def file(self, file_id):
        return '%s%s/src/%s' % (self._FILE_BASE,
                                self.board_id,
                                file_id)

    def thumb(self, file_id):
        return '%s%s/thumb/%ss.jpg' % (self._THUMB_BASE,
                                       self.board_id,
                                       file_id)
