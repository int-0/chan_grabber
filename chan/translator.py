#!/usr/bin/env python

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

class Translator(object):
    def __init__(self):
        pass

    def thread(self, thread_id):
        raise NotImplementedError()

    def file(self, file_id):
        raise NotImplementedError()
