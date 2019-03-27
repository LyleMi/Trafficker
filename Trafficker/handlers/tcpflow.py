#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TCPState(object):

    """TCPState"""

    # TCP_STATE || VALUE || TCP FLAGS
    CLOSE           = 0   # TH_RST | TH_ACK
    LISTEN          = 1   # 0
    SYN_SEND        = 2   # TH_SYN
    SYN_RECEIEVD    = 3   # TH_SYN | TH_ACK
    ESTABLISHED     = 4   #          TH_ACK
    CLOSE_WAIT      = 5   #          TH_ACK
    FIN_WAIT_1      = 6   # TH_FIN | TH_ACK
    CLOSING         = 7   # TH_FIN | TH_ACK
    LAST_ACK        = 8   # TH_FIN | TH_ACK
    FIN_WAIT_2      = 9   #          TH_ACK
    TIME_WATE       = 10  #          TH_ACK


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
            # print(reprself.tcps[-2], self.tcps[-4])
            self.finish = True

        if set([tcp.srcp, tcp.dstp]) != self.ports:
            return False

        last = self.tcps[-1]
        # SYN Sent
        if last.syn and not last.ack:
            if tcp.syn and tcp.ack and tcp.ackn == last.seqn+1:
                return True
        # SYN Recived
        elif last.syn and last.ack:
            if tcp.ack and tcp.seqn == last.ackn:
                return True
        # Established
        elif last.ack:
            if tcp.ackn == last.ackn and tcp.seqn == tcp.seqn:
                return True
            if tcp.ack and tcp.seqn == last.ackn:
                return True
            if tcp.ack and tcp.seqn == last.seqn and tcp.dstp == last.dstp:
                return True
        return False

    def extract(self):
        # TODO
        # TCP ZeroWindow
        # TCP Window Full
        # TCP Window Update
        # etc
        datas = []
        curp = self.tcps[0].srcp
        data = b""
        for t in self.tcps:
            if t.srcp == curp:
                data += t.payload
            else:
                if len(t.payload):
                    if len(data):
                        datas.append(data)
                    data = t.payload
                    curp = t.srcp
        if len(data):
            datas.append(data)
        return datas
