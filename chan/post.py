#!/usr/bin/env python3
# 
# Released under GPL3 license
#

'''
    A quick'n'dirty posts wrapper
'''

import chan.errors
import chan.request
import chan.reply_thread


class Post:
    '''Any post'''
    def __init__(self, translator, data):

        self.__translator = translator

        self.__id = data['no']
        self.__reply = data['resto']
        self.__date = data['time']

        # Optional

        # When OP is True
        self.__sticky = data.get('sticky', 0) == 1
        self.__closed = data.get('closed', 0) == 1

        # When DISPLAY_ID on board is set
        self.__author_id = data.get('id', 'anonymous')

        # If name is present
        self.__author_name = data.get('name', 'anonymous')

        # If tripcode is present
        self.__trip = data.get('trip', '!unknown')

        # If email is present
        self.__author_email = data.get('email', 'unknown')

        # If subject is present
        self.__subject = data.get('sub', '')

        # If comment is present
        self.__comment = data.get('com', '')

        # When using a capcode
        self.__author_class = data.get('capcode', 'anonymous')

        # If board uses country flags
        self.__country_code = data.get('country', 'xx')
        self.__country_name = data.get('country_name', 'Unknown')

        # When image is uploaded
        self.__rfile = data.get('tim', None)
        self.__ofile = data.get('filename', None)
        self.__ext = data.get('ext', None)
        self.__file_size = data.get('fsize', 0)
        self.__md5 = data.get('md5', '')
        self.__size = (data.get('w', 0), data.get('h', 0))
        self.__thumb_size = (data.get('tn_w', 0), data.get('tn_h', 0))
        self.__file_deleted = data.get('filedeleted', 0) == 1
        self.__is_spoiler = data.get('spoiler', 0) == 1

        # When board has custom spoilers
        self.__custom_spoiler = data.get('custom_spoiler', 0)

        # Only display on OPs
        self.__omited_posts = data.get('omitted_posts', 0)
        self.__omited_images = data.get('omitted_images', 0)
        self.__replies = data.get('replies', 0)
        self.__images = data.get('images', 0)

        # On OP when True
        self.__bump_limit = data.get('bumplimit', 0) == 1
        self.__image_limit = data.get('imagelimit', 0) == 1
       
    def __str__(self):
        return 'Post #%s (by %s):\n[%s]\n%s' % (self.__id,
                                                self.__author_name,
                                                self.__subject,
                                                self.__comment)
    def has_image(self):
        return self.__rfile is not None

    # def get_thumb(self):
    #     if not self.has_image():
    #         raise PostWithoutImage()
    #     return netapi.get_thumb(self.__board_id, self.__rfile)

    def get_image_remote_name(self):
        return self.__rfile

    def get_image_extension(self):
        return self.__ext

    def get_image(self):
        if not self.has_image():
            raise chan.errors.PostWithoutImage()
        return chan.request.to_file(self.__translator.file(self.__rfile, self.__ext))

    def get_image_name(self):
        if not self.has_image():
            raise chan.errors.PostWithoutImage()
        return '%s%s' % (self.__ofile, self.__ext)

    def get_image_size(self):
        if not self.has_image():
            raise chan.errors.PostWithoutImage()
        return self.__file_size
    
    @property
    def thread_id(self):
        return self.__id

    @property
    def subject(self):
        return self.__subject
        
    @property
    def board_id(self):
        return self.__translator.board_id

    @property
    def replies(self):
        return self.__replies

    def has_replies(self):
        return self.replies > 0

    def get_thread(self):
        if self.replies == 0:
            raise chan.errors.PostWithoutReplies()
        return chan.reply_thread.ReplyThread(self.__translator, self.thread_id)

