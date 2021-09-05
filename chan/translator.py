#!/usr/bin/env python

# A Translator() object converts thread-ids and file-ids
# into HTTP requests
#

MAX_PAGES = 50


class Translator:
    '''Generic translator'''
    def __init__(self, board_id, max_pages=MAX_PAGES):
        self.__board_id = board_id
        self.__max_pages = max_pages

    @property
    def max_pages(self):
        return self.__max_pages

    @property
    def board_id(self):
        return self.__board_id

    def thread(self, thread_id):
        raise NotImplementedError()

    def file(self, file_id):
        raise NotImplementedError()

    def thumb(self, file_id):
        raise NotImplementedError()


class T4Chan(Translator):
    '''Translator for 4Chan'''
    def __init__(self, board_id):
        super().__init__(board_id)
        self._API_URL = 'http://a.4cdn.org/'
        self._FILE_BASE = 'http://i.4cdn.org/'
        self._THUMB_BASE = 'http://s.4cdn.org/'

    def thread(self, thread_id):
        if thread_id < self.max_pages:
            # Root thread
            return f'{self._API_URL}{self.board_id}/{thread_id}.json'
        # Reply thread
        return f'{self._API_URL}{self.board_id}/res/{thread_id}.json'

    def file(self, file_id):
        return f'{self._FILE_BASE}{self.board_id}/src/{file_id}'

    def thumb(self, file_id):
        return f'{self._THUMB_BASE}{self.board_id}/thumb/{file_id}s.jpg'
