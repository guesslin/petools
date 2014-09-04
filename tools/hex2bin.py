#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import binascii


def hex_reorder(hexstr):
    '''convert 32-bits hex from transpose to bin'''
    elements = list()
    for n in xrange(0, len(hexstr), 8):
        elements.append(hexstr[n:n+8])

    raw = list()
    for item in elements:
        for n in xrange(len(item)-1, 0, -2):
            raw.append('{}{}'.format(item[n-1], item[n]))
    return ''.join(raw)


if __name__ == '__main__':
    hexstr = sys.argv[1]
    hexstr = hex_reorder(hexstr)
    hexbyte = binascii.a2b_hex(hexstr)

    with open('output.bin', 'wb') as binfile:
        binfile.write(hexbyte)
