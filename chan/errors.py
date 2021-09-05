#!/usr/bin/env python3

'''
    Common errors
'''
class BoardNotFound(Exception):
    '''Raised if wanted board not exists'''
    def __str__(self):
        return 'Board not found.'

class InvalidThread(Exception):
    '''Raised if wanted thread not exists'''
    def __init__(self, id):
        self.__id = id
    def __str__(self):
        return 'Unknown thread #id %s' % self.__id

class InvalidFile(Exception):
    '''Raised if wanted file not exists'''
    def __init__(self, id):
        self.__id = id
    def __str__(self):
        return 'Unknown file #id %s' % self.__id

class PostNotFound(Exception):
    '''Raised if wanted post not exists'''
    def __str__(self):
        return 'Post not found in board.'

class InvalidRequest(Exception):
    '''Raised on any HTTP request failure'''
    def __init__(self, reason='unknown reason'):
        self._reason_ = reason

    def __str__(self):
        return f'Unable to handle given request ({self._reason_})'

class PostWithoutImage(Exception):
    '''Raised when access to image post without image'''
    def __str__(self):
        return 'Post does not have images.'

class PostWithoutReplies(Exception):
    '''Raised when access to replies in a post without replies'''
    def __str__(self):
        return 'Post does not have replies.'

