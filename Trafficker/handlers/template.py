#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _defaultHandler(packetNum, packet, glob):
    """default packet handler

    Args:
        packetNum (int): packet number
        packet (obj): packet
        glob (dict): global dict

    Returns:
        dict: glob
    """
    print(packetNum, packet)
    return glob
