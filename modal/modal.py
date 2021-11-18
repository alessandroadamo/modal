import numpy as np
from collections import OrderedDict
from symbol import *
from chord import Chord


class Modal(object):
    __chromatic = np.array(
        ['C', flat + 'D', 'D', flat + 'E', 'E', 'F', flat + 'G', 'G', flat + 'A', 'A', flat + 'B', 'B'])
    __scales = ['major', 'melodic minor', 'harmonic major', 'harmonic minor']

    __major_scale_intervals = np.array([0, 2, 4, 5, 7, 9, 11])
    __melodic_minor_intervals = np.array([0, 2, 3, 5, 7, 9, 11])
    __harmonic_major_intervals = np.array([0, 2, 4, 5, 7, 8, 11])
    __harmonic_minor_intervals = np.array([0, 2, 3, 5, 7, 8, 11])
    # __melodic_minor_sharp5_intervals = np.array([0, 2, 3, 5, 8, 9, 11])
    # __ionic_sharp2_intervals = np.array([0, 3, 4, 5, 7, 9, 11])

    __shift_fun = np.vectorize(lambda x: x if x >= 0 else 12 + x)

    __chord = Chord()

    ###############
    # Major Scale #
    ###############
    major_modes = OrderedDict()
    major_modes['ionian'] = {
        'intervals': __major_scale_intervals,
        'triad_chord': __chord.find_triad_chord(__major_scale_intervals),
        '7th_chord': __chord.find_7th_chord(__major_scale_intervals)[0],
        '9th_chord': __chord.find_9th_chord(__major_scale_intervals),
        '11th_chord': __chord.find_11th_chord(__major_scale_intervals),
        '13th_chord': __chord.find_13th_chord(__major_scale_intervals),
    }
    major_modes['dorian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -1) - __major_scale_intervals[1])),
    }
    major_modes['phrygian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -2) - __major_scale_intervals[2])),
    }
    major_modes['lydian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -3) - __major_scale_intervals[3])),
    }
    major_modes['mixolydian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -4) - __major_scale_intervals[4])),
    }
    major_modes['aeonian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -5) - __major_scale_intervals[5])),
    }
    major_modes['locrian'] = {
        'intervals': __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__major_scale_intervals, -6) - __major_scale_intervals[6])),
    }

    #################
    # Melodic Minor #
    #################
    melodic_minor_modes = OrderedDict()
    melodic_minor_modes['ionian ' + flat + '3'] = {
        'intervals': __melodic_minor_intervals,
        'triad_chord': __chord.find_triad_chord(__melodic_minor_intervals),
        '7th_chord': __chord.find_7th_chord(__melodic_minor_intervals)[0],
        '9th_chord': __chord.find_9th_chord(__melodic_minor_intervals),
        '11th_chord': __chord.find_11th_chord(__melodic_minor_intervals),
        '13th_chord': __chord.find_13th_chord(__melodic_minor_intervals),
    }
    melodic_minor_modes['dorian ' + flat + '2'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -1) - __melodic_minor_intervals[1])),
    }
    melodic_minor_modes['lydian ' + sharp + '5'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -2) - __melodic_minor_intervals[2])),
    }
    melodic_minor_modes['lydian ' + flat + '7'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -3) - __melodic_minor_intervals[3])),
    }
    melodic_minor_modes['mixolydian ' + flat + '6'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -4) - __melodic_minor_intervals[4])),
    }
    melodic_minor_modes['locrian ' + natural + '2'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -5) - __melodic_minor_intervals[5])),
    }
    melodic_minor_modes['super locrian'] = {
        'intervals': __shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6])),
        '7th_chord':
            __chord.find_7th_chord(__shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6]))[
                0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__melodic_minor_intervals, -6) - __melodic_minor_intervals[6])),
    }

    ##################
    # Harmonic Major #
    ##################
    harmonic_major_modes = OrderedDict()
    harmonic_major_modes['ionian ' + flat + '6'] = {
        'intervals': __harmonic_major_intervals,
        'triad_chord': __chord.find_triad_chord(__harmonic_major_intervals),
        '7th_chord': __chord.find_7th_chord(__harmonic_major_intervals)[0],
        '9th_chord': __chord.find_9th_chord(__harmonic_major_intervals),
        '11th_chord': __chord.find_11th_chord(__harmonic_major_intervals),
        '13th_chord': __chord.find_13th_chord(__harmonic_major_intervals),
    }
    harmonic_major_modes['dorian ' + flat + '5'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -1) - __harmonic_major_intervals[1])),
    }
    harmonic_major_modes['phrygian ' + flat + '4'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -2) - __harmonic_major_intervals[2])),
    }
    harmonic_major_modes['lydian ' + flat + '3'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -3) - __harmonic_major_intervals[3])),
    }
    harmonic_major_modes['mixolydian ' + flat + '2'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -4) - __harmonic_major_intervals[4])),
    }
    harmonic_major_modes['lydian ' + sharp + '2 ' + sharp + '5'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -5) - __harmonic_major_intervals[5])),
    }
    harmonic_major_modes['locrian ' + flat + flat + '7'] = {
        'intervals': __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_major_intervals, -6) - __harmonic_major_intervals[6])),
    }

    ##################
    # Harmonic Minor #
    ##################
    harmonic_minor_modes = OrderedDict()
    harmonic_minor_modes['ionian ' + flat + '3' + ' ' + flat + '6'] = {
        'intervals': __harmonic_minor_intervals,
        'triad_chord': __chord.find_triad_chord(__harmonic_minor_intervals),
        '7th_chord': __chord.find_7th_chord(__harmonic_minor_intervals)[0],
        '9th_chord': __chord.find_9th_chord(__harmonic_minor_intervals),
        '11th_chord': __chord.find_11th_chord(__harmonic_minor_intervals),
        '13th_chord': __chord.find_13th_chord(__harmonic_minor_intervals),
    }
    harmonic_minor_modes['locrian 6'] = {
        'intervals': __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -1) - __harmonic_minor_intervals[1])),
    }
    harmonic_minor_modes['ionian ' + sharp + '5'] = {
        'intervals': __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -2) - __harmonic_minor_intervals[2])),
    }
    harmonic_minor_modes['dorian ' + flat + '11'] = {
        'intervals': __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -3) - __harmonic_minor_intervals[3])),
    }
    harmonic_minor_modes['phrygian dominant'] = {
        'intervals': __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -4) - __harmonic_minor_intervals[4])),
    }
    harmonic_minor_modes['lydian ' + sharp + '2'] = {
        'intervals': __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5]),
        'triad_chord': __chord.find_triad_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5])),
        '7th_chord': __chord.find_7th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -5) - __harmonic_minor_intervals[5])),
    }
    harmonic_minor_modes['super locrian ' + flat + flat + '7'] = {
        'intervals': __shift_fun(
            np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6]),
        'triad_chord': __chord.find_triad_chord(__shift_fun(
            np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6])),
        '7th_chord': __chord.find_7th_chord(__shift_fun(
            np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6]))[0],
        '9th_chord': __chord.find_9th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6])),
        '11th_chord': __chord.find_11th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6])),
        '13th_chord': __chord.find_13th_chord(
            __shift_fun(np.roll(__harmonic_minor_intervals, -6) - __harmonic_minor_intervals[6])),
    }

    def get_modes_name(self, scale: str) -> list | None:
        """
        Get modes names
        :param scale: scale name
            - 'major'
            - 'melodic minor'
            - 'harmonic major'
            - 'harmonic minor'
        :return:
        """
        modes = None
        if scale == 'major':
            modes = self.major_modes.keys()
        if scale == 'melodic minor':
            modes = self.melodic_minor_modes.keys()
        if scale == 'harmonic major':
            modes = self.harmonic_major_modes.keys()
        if scale == 'harmonic minor':
            modes = self.harmonic_minor_modes.keys()
        return modes

    def get_mode(self, root: str = 'C', scale: str = 'major', mode: int = 0):

        if root not in self.__chromatic:
            raise Exception('Not valid root note.')
        if scale not in self.__scales:
            raise Exception('Not supported scale.')
        if not (0 <= mode < 7):
            raise Exception('Not valid mode.')

        idx = np.where(self.__chromatic == root)[0]
        chrom = np.roll(self.__chromatic, -idx)

        sc = None
        if scale == 'major':
            sc = self.major_modes
        if scale == 'melodic minor':
            sc = self.melodic_minor_modes
        if scale == 'harmonic major':
            sc = self.harmonic_major_modes
        if scale == 'harmonic minor':
            sc = self.harmonic_minor_modes

        mode_name = list(sc.keys())[mode]
        md = {
            'mode name': root + ' ' + mode_name,
            'notes': chrom[sc[mode_name]['intervals']],
            'triad_chord': root + sc[mode_name]['triad_chord'],
            '7th_chord': root + sc[mode_name]['7th_chord'],
            '9th_chord': root + sc[mode_name]['9th_chord'],
            '11th_chord': root + sc[mode_name]['11th_chord'],
            '13th_chord': root + sc[mode_name]['13th_chord'],
        }
        return md

    def mode_harmonization(self, root: str = 'C', scale: str = 'major', mode: int = 0):

        modes = []
        md = self.get_mode(root=root, scale=scale, mode=mode)
        modes.append(md)

        for i in range(1, 7):
            modes.append(self.get_mode(root=md['notes'][i], scale=scale, mode=(mode+i)%7))

        return modes

    def print_mode_harmonization(self, root: str = 'C', scale: str = 'major', mode: int = 0):
        harm = self.mode_harmonization(root=root, scale=scale, mode=mode)

        table = '<center><b>' + harm[0]['mode name'].title() + '</b></center>\n\n'
        table += '| Chord |'
        table += 'i'+dim if harm[0]['triad_chord'].endswith('dim') else 'i' if harm[0]['triad_chord'].endswith('m') else 'I'
        table += '|'
        table += 'ii' + dim if harm[1]['triad_chord'].endswith('dim') else 'ii' if harm[1]['triad_chord'].endswith(
            'm') else 'II'
        table += '|'
        table += 'iii' + dim if harm[2]['triad_chord'].endswith('dim') else 'iii' if harm[2]['triad_chord'].endswith(
            'm') else 'III'
        table += '|'
        table += 'iv' + dim if harm[3]['triad_chord'].endswith('dim') else 'iv' if harm[3]['triad_chord'].endswith(
            'm') else 'IV'
        table += '|'
        table += 'v' + dim if harm[4]['triad_chord'].endswith('dim') else 'v' if harm[4]['triad_chord'].endswith(
            'm') else 'V'
        table += '|'
        table += 'vi' + dim if harm[5]['triad_chord'].endswith('dim') else 'vi' if harm[5]['triad_chord'].endswith(
            'm') else 'VI'
        table += '|'
        table += 'vii' + dim if harm[6]['triad_chord'].endswith('dim') else 'vii' if harm[6]['triad_chord'].endswith(
            'm') else 'VII'
        table += '|'
        table += '\n'

        table += '|--|--|--|--|--|--|--|--|\n'

        table += '| triad     |'
        for h in harm:
            table += h['triad_chord'] + '|'
        table += '\n'

        table += '| 7th     |'
        for h in harm:
            table += h['7th_chord'] + '|'
        table += '\n'

        table += '| 9th     |'
        for h in harm:
            table += h['9th_chord'] + '|'
        table += '\n'

        table += '| 11th     |'
        for h in harm:
            table += h['11th_chord'] + '|'
        table += '\n'

        table += '| 13th     |'
        for h in harm:
            table += h['13th_chord'] + '|'
        table += '\n'

        return table


if __name__ == '__main__':
    modal = Modal()

    sc = modal.get_mode('C', 'melodic minor', mode=0)

    for idx, r in enumerate(sc['notes']):
        print(modal.print_mode_harmonization(root=r, scale='melodic minor', mode=idx))
        print()
        print()


