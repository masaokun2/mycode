#!/usr/bin/env python3
import argparse
import socket
from datetime import datetime

def server(port,tran):
    x = "Your choice was server and it will run on " + str(tran) + " port " + str(port) 
    return x

def client(port,tran):
    x = "Your choice was client and it will run on " + str(tran) + " port " + str(port)
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='Port (default 1060)')
    parser.add_argument('-t', metavar='TRAN', type=str, default='UDP', help='Transmission Protocol (default UDP)')
    args = parser.parse_args()
    function = choices[args.role]
    print("args: ", args)
    print("function: ", function) 
    print(function(args.p,args.t))

