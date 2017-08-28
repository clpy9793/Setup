#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-01 10:35:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
install environment for centos7.2
"""
from __future__ import print_function
import os


os.system("yum -y groupinstall 'Development Tools'")
os.system("yum -y yum install zlib-devel bzip2-devel  openssl-devel ncurses-deve")
os.system('yum  -y install readline-devel')


os.system('rm Python-3.*.* -rf')
os.system("yum -y yum install zlib-devel bzip2-devel  openssl-devel ncurses-deve")
os.system('wget  https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz')
os.system('tar Jxvf  Python-3.6.2.tar.xz')
os.system('cd Python-3.6.2')
if not os.path.exists('/usr/local/python36'):
    os.system('mkdir /usr/local/python36')
os.system('./configure --prefix=/usr/local/python35')
os.system('make && make install')
os.system("echo 'export PATH=$PATH:/usr/local/python36/bin' >> ~/.bashrc")
