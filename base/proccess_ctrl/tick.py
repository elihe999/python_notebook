#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code
import time

def countdown(b):
    while b > 0:
        print('T-minus', b);
        b -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target = countdown, args = (10,))
t.start()
