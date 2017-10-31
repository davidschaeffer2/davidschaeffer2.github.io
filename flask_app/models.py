# app/models.py
# David Schaeffer
# 10/23/2017


import string


class PartyInformationLogic:
    @staticmethod
    def get_num_character_choices():
        num_characters_choices = []
        for i in range(1, 11):
            num_characters_choices.append((i, i))
        return num_characters_choices

    @staticmethod
    def get_player_level_choices():
        player_level_choices = []
        for i in range(1, 21):
            player_level_choices.append((i, i))
        return player_level_choices

    @staticmethod
    def get_difficulty_choices():
        difficulty_choices = [('easy', 'Easy'), ('average', 'Average'),
                              ('challenging', 'Challenging'), ('hard', 'Hard'),
                              ('epic', 'Epic')]
        return difficulty_choices

    @staticmethod
    def get_apl(num_chars, levels, difficulty):
        apl = 0
        for level in levels:
            if level is not None:
                apl += level
        apl = apl/num_chars
        if num_chars <= 3:
            apl -= 1
        elif num_chars >= 6:
            apl += 1
        if 'easy' in difficulty:
            apl -= 1
        elif 'average' in difficulty:
            pass
        elif 'challenging' in difficulty:
            apl += 1
        elif 'hard' in difficulty:
            apl += 2
        elif 'epic' in difficulty:
            apl += 3
        if apl < 1:
            apl = 1
        return apl

    @staticmethod
    def get_cr_exp_budget(apl):
        exp_values = [
            (0, 0),
            (1 / 8, 50),
            (1 / 6, 65),
            (1 / 4, 100),
            (1 / 3, 135),
            (1 / 2, 200),
            (1, 400),
            (2, 600),
            (3, 800),
            (4, 1200),
            (5, 1600),
            (6, 2400),
            (7, 3200),
            (8, 4800),
            (9, 6400),
            (10, 9600),
            (11, 12800),
            (12, 19200),
            (13, 25600),
            (14, 38400),
            (15, 51200),
            (16, 76800),
            (17, 102400),
            (18, 153600),
            (19, 204800),
            (20, 307200),
            (21, 409600),
            (22, 614400),
            (23, 819200),
            (24, 1228800),
            (25, 1638400),
            (26, 2457600),
            (27, 3276800),
            (28, 4915200),
            (29, 6553600),
            (30, 9830400)
        ]
        for cr, exp in exp_values:
            if cr == apl:
                return exp

    @staticmethod
    def get_alphabet():
        alphabet_list = []
        for char in string.ascii_uppercase:
            alphabet_list.append((char, char))
        return alphabet_list
