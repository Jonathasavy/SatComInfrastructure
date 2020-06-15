#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.httputil
import serial
from enum import Enum
from pymavlink import mavlink
import ConfigParser


MAV = mavlink.MAVLink(0)


def printmsg(data):
    m = None
    try:
        m = MAV.parse_buffer(data)
    except:
        pass
    if m is not None:
        for msg in m:
            print 'MAV MSG %3d %s' % (msg.get_msgId(), msg.get_type())
            print msg

def main():
    message = 'fd06000008ffbe0b000000000406010152b1'
    printmsg(message.decode('hex'))

if __name__ == '__main__':
    main()


