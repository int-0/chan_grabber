#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python

import common
import netapi
import board
import post

class ReplyThread(object):
    def __init__(self, src_board, thread_id):
        self.__thread_id = thread_id
        self.__board = src_board
        self.__main_api = '%s%s/res/%s.json' % (common.API_URL,
                                                self.__board,
                                                self.__thread_id)
        self.__posts = {}

    def refresh(self, clear = False):
        if clear:
            self.__posts = {}
        posts = netapi.fetch(self.__main_api)['posts']
        for post in posts:
            self.__posts[post['no']] = post
            
    def get_posts(self):
        return self.__posts.keys()

    def get_post(self, post_no):
        if post_no not in self.get_posts():
            raise board.PostNotFound()
        return post.Post(self.__posts[post_no], self.__board)

    def __contains__(self, post_no):
        assert(isinstance(post_no, int))
        return post_no in self.get_posts()
