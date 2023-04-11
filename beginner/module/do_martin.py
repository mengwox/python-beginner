#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """
__author__ = 'mawenhao'

import sys

import private


def test():
    args = sys.argv
    la = len(args)
    print()
    if la == 1:
        print('hello world!')
    elif la == 2:
        print('hello %s!' % args[1])
    else:
        print('too many arguments')
    private.greeting("name")


if __name__ == '__main__':
    test()
