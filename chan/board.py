#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python3

import chan.post
import chan.errors
import chan.request

class Board:
    '''Forum board wrapper'''
    def __init__(self, translator):
        self.__translator = translator
        self.__posts = {}

    @property
    def translator(self):
        return self.__translator

    def update(self, clear = False):
        if clear:
            self.__posts = {}

        for page in range(1, self.__translator.max_pages):
            try:
                threads = chan.request.to_api(self.__translator.thread(page))['threads']
            except chan.errors.InvalidRequest:
                break

            for thread in threads:
                for post in thread['posts']:
                    self.__posts.update({post['no'] : post})

    def get_posts(self):
        return list(self.__posts.keys())

    def get_post(self, post_no):
        if post_no not in self.get_posts():
            raise chan.errors.PostNotFound()
        return chan.post.Post(self.__translator, self.__posts[post_no])

    def __contains__(self, post_no):
        assert(isinstance(post_no, int))
        return post_no in self.get_posts()
