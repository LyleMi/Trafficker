#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ipFilter(packetNum, packet, glob, white=[]):
    '''Filter for Traffic

    Args:
        packetNum (int): packet number
        packet (obj): packet
        glob (dict): global dict
        white (dict, optional): white list

    Returns:
        bool: if True do not hanlde that packet
    '''
    return packet.srcip in white or packet.dstip in white
