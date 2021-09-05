#
# PYCHAN
# 
# Released under GPL3 license
#
#!/usr/bin/env python3

import chan.board
import chan.errors
import chan.request
import chan.translator

class B4Chan:
    def __init__(self):
        self.__boards = {}

    def open(self):
        data = chan.request.to_api('http://a.4cdn.org/boards.json')
        for board_data in data['boards']:
            self.__boards[board_data['board']] = {
                'title' : board_data.get('title', 'unknown'),
                'pages' : board_data.get('pages', -1),
                'archived': board_data.get('is_archived', False)
                }

    def get_available_boards(self):
        return self.__boards.keys()

    def get_board_title(self, board_id):
        return self.__boards.get(board_id, {'title' : None})['title']

    def get_board(self, bid):
        ch = chan.translator.T4Chan(bid)
        if bid not in self.__boards.keys():
            raise chan.errors.BoardNotFound()
        return chan.board.Board(ch)
