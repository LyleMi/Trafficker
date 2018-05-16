#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from layer import layer


class DNSBase(layer):

    class QTYPE:
        TA = 32768
        A = 1
        NS = 2
        CNAME = 5
        SOA = 6
        DLV = 32769
        PTR = 12
        MX = 15
        TXT = 16
        RP = 17
        AFSDB = 18
        SPF = 99
        SIG = 24
        KEY = 25
        AAAA = 28
        LOC = 29
        SRV = 33
        NAPTR = 35
        KX = 36
        CERT = 37
        DNAME = 39
        OPT = 41
        APL = 42
        DS = 43
        SSHFP = 44
        IPSECKEY = 45
        RRSIG = 46
        NSEC = 47
        DNSKEY = 48
        DHCID = 49
        NSEC3 = 50
        NSEC3PARAM = 51
        HIP = 55
        TKEY = 249
        TSIG = 250
        IXFR = 251
        AXFR = 252
        DEFAULT = 255

    class CLASS:
        IN = 1
        CS = 2
        CH = 3
        Hesiod = 4
        NONE = 254
        DEFAULT = 255

    class QR:
        QUERY = 0
        RESPONSE = 1

    class RCODE:
        NONE = 0
        FormatError = 1
        Serverfailure = 2
        NAMEERROR = 3
        NOTIMPLEMENTED = 4
        Refused = 5
        YXDOMAIN = 6
        YXRRSET = 7
        NXRRSET = 8
        NOTAUTH = 9
        NOTZONE = 10

    class OPCODE:
        QUERY = 0
        IQUERY = 1
        STATUS = 2
        UPDATE = 5

    def __init__(self, dns=None):
        pass


class DNSHeader(DNSBase):

    def __init__(self, data=None):
        super(DNSHeader, self).__init__()

    @staticmethod
    def unpack(data):
        dnsHeader = DNSHeader()
        data = struct.unpack("!HHHHHH", data)
        dnsHeader.transid = data[0]
        dnsHeader.flags = data[1]
        dnsHeader.questions = data[2]
        dnsHeader.answer = data[3]
        dnsHeader.authority = data[4]
        dnsHeader.additional = data[5]
        return dnsHeader


class DNSQuery(DNSBase):

    @staticmethod
    def unpack(data):
        query = DNSQuery()
        query.qname = data.decodeName()
        query.qtype, query.qclass = data.unpack("!HH")
        return query


class DNS(DNSBase):

    @staticmethod
    def unpack(data):
        dns = DNS()
        dns.header = DNSHeader.unpack(data.get(12))
        dns.queries = []
        for i in range(dns.header.questions):
            dns.queries.append(DNSQuery.unpack(data))
        # todo
        # parse answer, authorities, additionals
        return dns

    def __repr__(self):
        return "<DNS %s>" % (
            ";".join(map(lambda i: i.qname, self.queries))
        )

    @property
    def domains(self):
        return list(set(map(lambda i: i.qname, self.queries)))

if __name__ == '__main__':
    pass
