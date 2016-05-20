#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def hex2string(hex_list):
    for h in hex_list:
        print h.decode('hex')


def string2hex(string_list):
    for s in string_list:
        print s.encode('hex')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='string input, '
                        'default action for translate to hex',
                        action='append')
    parser.add_argument('-s', '--string', action='store_true')
    parser.parse_args()
