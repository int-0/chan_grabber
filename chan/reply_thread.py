#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python

import request
import board
import post

class ReplyThread(object):
    def __init__(self, translator, thread_id):
        self.__translator = translator
        self.__thread_id = thread_id
        self.__posts = {}

    def update(self, clear = False):
        if clear:
            self.__posts = {}
        posts = request.to_api(self.__translator.thread(self.__thread_id))
        posts = posts['posts']
        for post in posts:
            self.__posts.update({post['no']: post})
            
    def get_posts(self):
        return self.__posts.keys()

    def get_post(self, post_no):
        if post_no not in self.get_posts():
            raise board.PostNotFound()
        return post.Post(self.__translator, self.__posts[post_no])

    def __contains__(self, post_no):
        assert(isinstance(post_no, int))
        return post_no in self.get_posts()
