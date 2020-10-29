3 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# packer.py
# A demo program for lora to send message compatible with python2/3
#
# Author : sosorry
# Date   : 10/03/2017
#

import codecs

decode_hex = codecs.getdecoder("hex_codec")

SOH  = "01"    # 0x01
ACK  = "06"    # 0x06
CRLF = "\r\n"  # 0x32 0x41 0x33 0x31

#
# pack string to customized payload
#
# payload: [SOH]    [LENGTH]   [PAYLOAD]          [CRLF]
#          2 bytes  6 bytes    length * 2 bytes   4 bytes
#
def Pack_Str(string):
    data   = string.encode("utf-8").hex()
    length = len(data)

    if length < 10:
        length = str(0) + str(0) + str(length)
    elif length >= 10 and length < 100:
        length = str(0)  + str(length)
    else:
        length = str(length)

    length = length.encode("utf-8").hex()
    payload = SOH + str(length) + data + CRLF
    #print("RAW: " + payload)

    return [length, payload]


#
# unpack payload to string
#
def Unpack_Str(string):
    soh    = string[0:1]
    length = decode_hex(string[2:8]) /2
    data   = decode_hex(string[8:-2])[0]

    return [length, data]

