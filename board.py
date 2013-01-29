#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python

import common
import netapi
import post

class PostNotFound(Exception):
    def __str__(self):
        return 'Post not found in board.'

class Board(object):
    def __init__(self, board_id):
        self.__main_api = '%s%s/0.json' % (common.API_URL, board_id)
        self.__board = board_id
        self.__posts = {}

    def refresh(self, clear = False):
        if clear:
            self.__posts = {}
        self.__threads = netapi.fetch(self.__main_api)['threads']
        for thread in self.__threads:
            for post in thread['posts']:
                self.__posts[post['no']] = post

    def get_posts(self):
        return self.__posts.keys()

    def get_post(self, post_no):
        if post_no not in self.get_posts():
            raise PostNotFound()
        return post.Post(self.__posts[post_no], self.__board)

    def __contains__(self, post_no):
        assert(isinstance(post_no, int))
        return post_no in self.get_posts()
