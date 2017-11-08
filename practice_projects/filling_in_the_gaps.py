#!python3
# filling_in_the_gaps.py - finds all files with a given prefix, such as
# `spam001.txt`, spam002.txt, and so on, in a single folder and locates any
# gaps in the numbering. Have the program rename all the later files to close
# this gap.
# write another program that can insert gaps into numbered files so that a new
# file can be added.

import os
import shutil
import re
import random
import pathlib


def gengap(fd, prefix, n):
    os.chdir(fd)
    for f in os.listdir('.'):
        os.unlink(f)

    smp = random.sample(range(1, 100), n)
    for idx in smp:
        newfile = os.path.join('.', prefix + str(idx).zfill(3) + '.txt')
        pathlib.Path(newfile).touch()


def fillgap(fd, prefix):
    os.chdir(fd)
    reg = re.compile(r'^%s(\d+)' % prefix)
    n = -1
    sz = -1
    for filename in os.listdir('.'):
        mo = reg.search(filename)
        if mo is not None:
            if n == -1 and sz == -1:
                n = int(mo.group(1))
                sz = len(str(mo.group(1)))
            else:
                n += 1
                newname = prefix + str(n).zfill(sz) +
                os.path.splitext(filename)[1]
                shutil.move(filename, newname)


def insertgap(fd, prefix):
    os.chdir(fd)
    reg = re.compile(r'^%s(\d+)' % prefix)
    for filename in os.listdir('.'):
        mo = reg.search(filename)
        if mo is not None:
            n = int(mo.group(1))
            sz = len(str(mo.group(1)))
            newfile = os.path.join('.', prefix + str(n).zfill(sz) +
                                   os.path.splitext(filename)[1])
            while os.path.exists(newfile):
                n += 1
                newfile = os.path.join('.', prefix + str(n).zfill(sz) +
                                       os.path.splitext(filename)[1])
            pathlib.Path(newfile).touch()
            break


curpath = os.getcwd()

# os.chdir(curpath)
# gengap('test', 'spam', 9)

# os.chdir(curpath)
# insertgap('test', 'spam')

os.chdir(curpath)
fillgap('test', 'spam')
