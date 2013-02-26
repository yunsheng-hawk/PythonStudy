'''
Created on 2013-2-21

@author: huysh1976
'''
import os
import time
source='D:\\var\\log\\tomcat\\alpha.nsp.log'
target='D:\\bak\\alpha.nsp.log'
cmd='copy %s %s' % (source, target)
if os.system(cmd) == 0:
    print 'bakup finished.'
