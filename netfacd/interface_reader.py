#! /usr.bin/env python3

import netifaces

def ipaddress(adaptername):
    return (netifaces.ifaddresses(adaptername)[netifaces.AF_LINK][0]['addr'])

def macaddress(adaptername):
    return (netifaces.ifaddresses(adaptername)[netifaces.AF_INET][0]['addr'])

def main():
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end='')
            print(ipaddress(i))
            print('IP: ', end='')
            print(ipaddress(i))
        except:
            print("Could not collect adapter information")


main()
