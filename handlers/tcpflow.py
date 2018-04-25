#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TCPFlow(object):

    """tcp flow

    Attributes:
        srcp (int): tcp syn packet source port
    """

    def __init__(self, syn):
        """Summary

        Args:
            syn (tcp): syn init tcp packet
        """
        super(TCPFlow, self).__init__()
        self.srcp = syn.srcp
        self.dstp = syn.dstp
        self.ports = set([self.srcp, self.dstp])
        self.tcps = [syn]
        self.finish = False

    def isNext(self, tcp):

        if self.finish:
            return False

        if len(self.tcps) >= 4 and self.tcps[-2].fin and self.tcps[-4].fin:
            print(self.tcps[-2], self.tcps[-4])
            self.finish = True

        if set([tcp.srcp, tcp.dstp]) != self.ports:
            return False

        last = self.tcps[-1]
        # just init
        if last.syn and not last.ack:
            if tcp.syn and tcp.ack and tcp.ackn == last.seqn+1:
                return True
        # stage 2
        elif last.syn and last.ack:
            if tcp.ack and tcp.seqn == last.ackn:
                return True
        elif last.ack:
            if tcp.ackn == last.ackn and tcp.seqn == tcp.seqn:
                return True
            if tcp.ack and tcp.seqn == last.ackn:
                return True
            if tcp.ack and tcp.seqn == last.seqn and tcp.dstp == last.dstp:
                return True
        return False
