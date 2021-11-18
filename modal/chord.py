import numpy as np
from symbol import *


class Chord(object):
    ##########
    # triads #
    ##########
    triads = {
        'maj_chord': {
            'intervals': np.array([0, 4, 7]),
            'symbol': 'maj'
        },
        'min_chord': {
            'intervals': np.array([0, 3, 7]),
            'symbol': 'm'
        },
        'dim_chord': {
            'intervals': np.array([0, 3, 6]),
            'symbol': 'dim'
        },
        'aug_chord': {
            'intervals': np.array([0, 4, 9]),
            'symbol': 'aug'
        },
        'sus2_chord': {
            'intervals': np.array([0, 2, 7]),
            'symbol': 'sus2'
        },
        'sus4_chord': {
            'intervals': np.array([0, 5, 7]),
            'symbol': 'sus4'
        }
    }
    ##############
    # 7th chords #
    ##############
    chords7th = {
        'maj7_chord': {
            'intervals': [0, 4, 7, 11],
            'symbol': 'maj7'
        },
        'min_maj7_chord': {
            'intervals': [0, 3, 7, 11],
            'symbol': 'm(maj7)'
        },
        'min7_chord': {
            'intervals': [0, 3, 7, 10],
            'symbol': 'm7'
        },
        'dom7_chord': {
            'intervals': [0, 4, 7, 10],
            'symbol': '7'
        },
        'aug7_chord': {
            'intervals': [0, 4, 8, 11],
            'symbol': 'aug7'
        },
        'dim7_chord': {
            'intervals': [0, 3, 6, 9],
            'symbol': 'dim7'
        },
        'halfdim7_chord': {
            'intervals': [0, 3, 6, 10],
            'symbol': 'm7'+flat+'5'
        },
        'sus7_chord': {
            'intervals': [0, 5, 7, 10],
            'symbol': 'sus7'
        }
    }

    def find_triad_chord(self, intervals: np.array) -> str | None:
        """
        Find the triad chord
        :param intervals: scale intervals
        :return: chord symbol
        """
        symbol = None
        for triad in self.triads.keys():
            if np.isin(intervals, self.triads[triad]['intervals']).sum() == 3:
                symbol = self.triads[triad]['symbol']
                break
        return symbol

    def find_7th_chord(self, intervals: np.array) -> tuple:
        """
        Find the 7th chord
        :param intervals: scale intervals
        :return: chord symbol and diff array
        """
        symbol = None
        diff = None
        for chord in self.chords7th.keys():
            if np.isin(intervals, self.chords7th[chord]['intervals']).sum() == 4:
                symbol = self.chords7th[chord]['symbol']
                diff = intervals[np.logical_not(np.isin(intervals, self.chords7th[chord]['intervals']))]
                break
        return symbol, diff

    def find_9th_chord(self, intervals: np.array) -> str | None:
        """
        Find the 9th chord
        :param intervals: scale intervals
        :return: chord symbol
        """
        symbol, diff = self.find_7th_chord(intervals)
        check = self.check9th(diff)

        if check == '9':
            symbol = symbol.replace('7', '9')
        else:
            symbol += '(' + check + ')'
        return symbol

    def find_11th_chord(self, intervals: np.array) -> str | None:
        """
        Find the 11th chord
        :param intervals: scale intervals
        :return: chord symbol
        """
        symbol, diff = self.find_7th_chord(intervals)
        check9th = self.check9th(diff)
        check11th = self.check11th(diff)

        if check9th == '9':
            if check11th == '11':
                symbol = symbol.replace('7', '11')
            else:
                symbol = symbol.replace('7', '9')
                symbol += '(' + check11th + ')'
        else:
            symbol += '(' + check9th + ',' + check11th + ')'
        return symbol

    def find_13th_chord(self, intervals: np.array) -> str | None:
        """
        Find the 13th chord
        :param intervals: scale intervals
        :return: chord symbol
        """
        symbol, diff = self.find_7th_chord(intervals)
        check9th = self.check9th(diff)
        check11th = self.check11th(diff)
        check13th = self.check13th(diff)

        if check9th == '9':
            if check11th == '11':
                if check13th == '13':
                    symbol = symbol.replace('7', '13')
                else:
                    symbol = symbol.replace('7', '11')
                    symbol += '(' + check13th + ')'
            else:
                symbol = symbol.replace('7', '9')
                symbol += '(' + check11th + ',' + check13th + ')'
        else:
            symbol += '(' + check9th + ',' + check11th + ',' + check13th + ')'
        return symbol

    @staticmethod
    def check9th(intervals):
        val = None
        if 2 in intervals:
            val = '9'
        if 1 in intervals:
            val = flat + '9' if val is None else val + ',' + flat + '9'
        if 3 in intervals:
            val = sharp + '9' if val is None else val + ',' + sharp + '9'
        return val

    @staticmethod
    def check11th(intervals):
        val = None
        if 5 in intervals:
            val = '11'
        if 4 in intervals:
            val = flat + '11' if val is None else val + ',' + flat + '11'
        if 6 in intervals:
            val = sharp + '11' if val is None else val + ',' + sharp + '11'
        return val

    @staticmethod
    def check13th(intervals):
        val = None
        if 9 in intervals:
            val = '13'
        if 8 in intervals:
            val = flat + '13' if val is None else val + flat + '13'
        if 10 in intervals:
            val = sharp + '13' if val is None else val + sharp + '13'
        return val


if __name__ == '__main__':

    chord = Chord()

    print(chord.find_triad_chord(np.array([0, 2, 4, 5, 7, 9, 11])))
    print(chord.find_7th_chord(np.array([0, 2, 4, 5, 7, 9, 11])))
    print(chord.check9th(np.array([0, 2, 4, 5, 7, 9, 11])))
    print(chord.check11th(np.array([0, 2, 4, 5, 6, 7, 9, 11])))
    print(chord.check13th(np.array([0, 2, 4, 5, 6, 7, 9, 11])))


