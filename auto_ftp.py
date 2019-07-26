#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ftplib import FTP
import sys

def login():
    return FTP("10.11.1.13", 'secplatform', '123ABCdef*')

def updown(flag, path, files):
    ftp = login()
    ftp.cwd(path)
    for f in files:
        if flag = 'up':
            with open(f) as fp:
                print ftp.storbinary('STOR ' + f, fp)
        else:
            with open(f) as fp:
                print ftp.retrbinary('RETR ' + f, fp.write)
    ftp.close()
    return


def mkd(new_path):
    ftp = login()
    print ftp.mkd(new_path)
    ftp.close()


def usage():
    print 'Usage:'
    print '     auto_ftp.py up <upload path> <filename1> <filename2> ...'
    print '     auto_ftp.py down <download path> <filename1> <filename2> ...'
    print '     auto_ftp.py mkd <new path>'
    exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()

    flag = sys.argv[1]
    path = sys.argv[2]
    file_list = sys.argv[3:]

    if flag == 'up' or flag == 'down':
        if len(sys.argv) < 4:
            usage()
        upload(path, file_list)
    elif flag == 'mkd':
        mkd(path)
    else:
        usage()
