import requests as r
import time
import urllib3
import http.client as httplib
import sys
import colorama
import socket
from colorama import *
colorama.init()
yes_choice = ['','Yes', 'y', 'Y', 'yes', 'YES']
no_choice = ['No', 'n', 'no', 'NO', 'N']

def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='Insert the target URL')
    parser.add_argument('-o', '--output', type=str, metavar='', required=False, help='Create an output file')
    return parser.parse_args()


def banner():
    print(Fore.GREEN+f"""
    
    Coded By: Mata
    
    Subdomain finder without wordlist.

    Searching in all Browsers🔍

    COUNTRY: Greece🔵⚪

     
    
    
    """+Fore.RESET)

def check_updates():
    try:
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "/MataGreek/ypodomainfind3r/main/core/version.txt")
        neover = conn.getresponse().read().strip().decode()
        with open('./core/version.txt') as vf:
            torinover = vf.read().strip()
        if neover == torinover:
            print("")
        else:
            ask = input("[+] Version "+str(neover)+" is available. Do you want to update? [Y/n]:  ")
            if ask in yes_choice:
                print("")
                print("[!] Updating. Please do not close your application.")
                print("")
                time.sleep(1)

                try:
                    conn.request("GET", "/MataGreek/ypodomainfind3r/main/ypodomainfind3r.py")
                    neoskod = conn.getresponse().read().strip().decode()
                    with open('ypodomainfind3r.py', 'w+') as yp:
                        torinoyp = yp.read().strip()
                        if  neoskod != torinoyp:

                            yp.write(neoskod)
                    print("")
                    print("[+] Updated!")
                    time.sleep(1)
                    print("")
                    pass

                    if neover != torinover:
                        with open('./core/version.txt', 'w+') as pf:
                            pf.write(neover)
                    else:
                        print(Fore.RED + " [!] Your version is:", torinover + "You are not up to date! Please update the program." + Fore.GREEN)
                except KeyboardInterrupt:
                    print("exit")
    except Exception as e:
        print("Error: ", e)




def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print("damn")
        sys.exit(1)
    return host

def write_file(subdomain, output_file):
    with open('./output/'+output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        fp.close()

def main():
    check_updates()
    banner()
    time.sleep(1)
    subdomains = []
    args = parse_args()
    target = parse_url(args.url)
    output  = args.output

    req = r.get(f"https://crt.sh/?q=%.{target}&output=json")

    if req.status_code != 200:
        print("info not available")
        sys.exit(1)

    for (key,value) in enumerate(req.json()):
        subdomains.append(value['name_value'])
    print(f'\n target: {target}\n')
    ip = socket.gethostbyname(target)
    print(' Ip: ', ip+'\n\n\n')
    subs = sorted(set(subdomains))
    for s in subs:
        print(f'{s}')
        if output is not None:
            write_file(s, output)

    print("\n\nCompleted")

if __name__ == '__main__':
    main()


