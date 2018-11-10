#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _defaultFilter(packetNum, packet, glob):
    '''Filter for Traffic

    Args:
        packetNum (int): packet number
        packet (obj): packet
        glob (dict): global dict

    Returns:
        bool: if True do not hanlde that packet
    '''
    return False
