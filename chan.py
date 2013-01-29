#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python

import common
import netapi
import board

class BoardNotFound(Exception):
    def __str__(self):
        return 'Board not found.'

class B4Chan(object):
    def __init__(self):
        self.__chan_api = common.API_URL + 'boards.json'
        self.__boards = {}

    def open(self):
        data = netapi.fetch(self.__chan_api)
        for board_data in data['boards']:
            self.__boards[board_data['board']] = {
                'title' : board_data.get('title', 'unknown'),
                'pages' : board_data.get('pages', -1)
                }

    def get_available_boards(self):
        return self.__boards.keys()

    def get_board_title(self, board_id):
        return self.__boards.get(board_id, {'title' : None})['title']

    def get_board(self, bid):
        if bid not in self.__boards.keys():
            raise BoardNotFound()
        return board.Board(bid)

