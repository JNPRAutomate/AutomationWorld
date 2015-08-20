#! /usr/bin/env python

import netaddr
import string
import argparse
import xmltodict
from jnpr.junos.utils.config import Config
from jnpr.junos import Device
import xml.etree.ElementTree as ET
import pprint

'''
Usage:

python checker.py  --host <host> --username <username> --password <password> --subnet 2.0.0.0/24

Specify the subnet in bit mask format such as: 2.0.0.0/24

Interface et-0/0/1 is compliant with subnet: True
Interface et-0/0/2 is compliant with subnet: True
Interface et-0/0/3 is compliant with subnet: True
Interface et-0/0/69 is compliant with subnet: True
Interface irb is compliant with subnet: True
'''

def check_ip_in_subnet(ip,subnet):
    ipaddr = netaddr.IPAddress(ip)
    ipnet = netaddr.IPNetwork(subnet)

    if int(ipaddr) >= ipnet.first and int(ipaddr) <= ipnet.last:
        return True
    else:
        return False

parser = argparse.ArgumentParser(description='Process user input')
parser.add_argument("--host", dest="hostname", default="",metavar="HOST",help="Specify host to connect to")
parser.add_argument("--username", dest="username", metavar="USERNAME",help="Specify the username")
parser.add_argument("--password", dest="password", metavar="PASSWORD",help="Specify the password")
parser.add_argument("--subnet", dest="subnet", metavar="SUBNET",help="Specify the subnet to check interfaces against")
args = parser.parse_args()

if args.hostname != "" and args.username != "" and args.password != "":
    dev = Device(user=args.username, host=args.hostname, password=args.password)
    dev.bind(cu=Config)
    dev.open()
    cfg = dev.rpc.get_config()
    dd = xmltodict.parse(ET.tostring(cfg,encoding="utf8", method="xml"))

    if "configuration" in dd:
        if "interfaces" in dd["configuration"]:
            if "interface" in dd["configuration"]["interfaces"]:
                for i in dd["configuration"]["interfaces"]["interface"]:
                    if "unit" in i:
                        if "family" in i["unit"]:
                            if "inet" in i["unit"]["family"]:
                                if "address" in i["unit"]["family"]["inet"]:
                                    if "name" in i["unit"]["family"]["inet"]["address"]:
                                        int_name = i["name"]
                                        test_ip = string.split(i["unit"]["family"]["inet"]["address"]["name"],"/")[0]
                                        print "Interface {0} is compliant with subnet: {1}".format(int_name,check_ip_in_subnet(test_ip,args.subnet))
else:
    print "Unable to connect to host"
