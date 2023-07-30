import requests
import re
from termcolor import colored

def validate_ip(ip):
    pattern = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    return bool(pattern.match(ip))

def get_ip_info(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,continent,country,region,regionName,city,zip,lat,lon,timezone,isp,query')
    return response.json()

def print_ip_info(ip_info):
    excluded_keys = ['status', 'continentCode', 'countryCode']
    longest_key = max((k for k in ip_info.keys() if k not in excluded_keys), key=len)

    for key, value in ip_info.items():
        if key not in excluded_keys:
            print(colored(f'{key.title():<{len(longest_key)+1}}', 'blue') + colored(f'{value}', 'white'))

def main():
    print(colored('''
 ██████╗ █████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║     ███████║   ██║       ███████╗██║     ███████║██╔██╗ ██║
██║     ██╔══██║   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
╚██████╗██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║    
                                                                     ''', 'green'))
    print("---------------------------------------------------------------")
    print(colored("Terminal Based IP Address Lookup Tool", 'yellow'))
    print(colored("https://github.com/mrcafune | https://kittentechnologies.com", 'green'))
    print("---------------------------------------------------------------\n")

    while True:
        ip = input("WAN IP address: ")
        if validate_ip(ip):
            print("")
            ip_info = get_ip_info(ip)
            print_ip_info(ip_info)
            break
        else:
            print(colored("Invalid IP address, please try again.", 'red'))
            print("")

if __name__ == "__main__":
    main()
