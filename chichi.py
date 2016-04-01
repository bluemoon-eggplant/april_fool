# -*- coding: utf-8 -*-

import csv

# under * top --> cup
size2cup = dict()
reader = csv.reader(open('cup_predict.csv'))
next(reader, None)
for row in reader:
    under, top, cup = row
    size2cup[(int(under), int(top))] = cup

# secret value
MAX_UNDER = 110
MAX_TOP = 125
MIN_UNDER = 60
MIN_TOP = 68

# actress --> cup
actress2cup = dict()
reader = csv.reader(open('cup_size.csv'))
next(reader, None)
for row in reader:
    _, actress, cup = row
    actress2cup[actress] = cup.split()[0]

# actress --> size (in actress2cup)
reader = csv.reader(open('three_size.csv'))
next(reader, None)
for row in reader:
    _, actress, size = row
    if not actress in actress2cup:
        actress2cup[actress] = size.split()[0]

# command --> response
command2resp = dict()
reader = csv.reader(open('oppai.chikubi.csv'))
next(reader, None)
for row in reader:
    command, resp = row
    command2resp[command] = resp


class ChiPaiException(Exception):
    pass
class MeloChiChiException(Exception):
    pass
class NotDoingAnythingException(Exception):
    pass
class UnknownChiChiException(Exception):
    pass


def __fetch_actress_cup(actress):
    if not actress in actress2cup:
        return 'Have not Oppai!'
    return actress2cup[actress]


def pipi(actress=None):
    if not actress:
        return 'Hello World!'
    return __fetch_actress_cup(actress)


def __pipi_x(i, actress=None):
    sizes = pipi(actress)
    size = sizes.split('/')[i][1:]
    return int(size)


def pipi_bust(actress=None):
    return __pipi_x(0, actress)


def pipi_west(actress=None):
    return __pipi_x(1, actress)


def pipi_hip(actress=None):
    return __pipi_x(2, actress)


def chikubi(command):
    if not command in command2resp:
        raise NotDoingAnythingException("It lonely if you do not do something. ChiChi are not so much afraid.")
    return command2resp[command]


def cup_predict(under, top):
    if (under < MIN_UNDER) and (top < MIN_TOP):
        raise ChiPaiException('Is child? This is my kind of love also.')
    elif (under > MAX_UNDER) and (top > MAX_TOP):
        raise MeloChiChiException('This ChiChi is too large. And this tits dream is clogged.')
    if not (under, top) in size2cup:
        raise UnknownChiChiException('Never seen such ChiChi! There is a dream :)')
    cup = size2cup[(int(under), int(top))]
    if cup == 'unknown':
        raise UnknownChiChiException('Never seen such ChiChi! There is a dream :)')
    return cup


def main():
    pass


if __name__ == '__main__':
    main()
