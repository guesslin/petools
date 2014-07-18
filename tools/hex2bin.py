# -*- coding: utf-8 -*-
import sys
import binascii


def hex_reorder(hexstr):
    elements = list()
    for i in xrange(0, len(hexstr), 8):
        elements.append(hexstr[i:i+8])

    raw = list()
    for i in elements:
        for n in xrange(len(i)-1, 1, -2):
            raw.append('{}{}'.format(i[n-1], i[n]))
    return ''.join(raw)


if __name__ == '__main__':
    hexstr = sys.argv[1]
    hexstr = hex_reorder(hexstr)
    hexbyte = binascii.a2b_hex(hexstr)

    with open('output.bin', 'wb') as binfile:
        binfile.write(hexbyte)
