from os import *
from sys import *
from requests import *
from time import *

def ip_track(ip=""):
    ip_data = get('http://ip-api.com/json/'+ip).json()
    try:status = ip_data['status']
    except:status = " - "
    try:country = ip_data['country']
    except:country = " - "
    try:countryCode = ip_data['countryCode']
    except:countryCode = " - "
    try:region = ip_data['region']
    except:region = " - "
    try:regionName = ip_data['regionName']
    except:regionName = " - "
    try:city = ip_data['city']
    except:city = " - "
    try:zip = ip_data['zip']
    except:zip = " - "
    try:lat = ip_data['lat']
    except:lat = " - "
    try:lon = ip_data['lon']
    except:lon = " - "
    try:timezone = ip_data['timezone']
    except:timezone = " - "
    try:isp = ip_data['isp']
    except:isp = " - "
    try:org = ip_data['org']
    except:org = " - "
    try:asa = ip_data['as']
    except:asa = " - "
    try:query = ip_data['lat']
    except:query = " - "
    print(f"\n[*] Status : {status}")
    print(f"[*] Country : {country}")
    print(f"[*] CountryCode : {countryCode}")
    print(f"[*] Region : {region}")
    print(f"[*] RegionName : {regionName}")
    print(f"[*] City : {city}")
    print(f"[*] Zip : {zip}")
    print(f"[*] Lat : {lat}")
    print(f"[*] Lon : {lon}")
    print(f"[*] TimeZone : {timezone}")
    print(f"[*] ISP : {isp}")
    print(f"[*] ORG : {org}")
    print(f"[*] As : {asa}")
    print(f"[*] Query : {query}\n")


if len(argv)==2:
    if argv[1] in ['-info','--info']:
        print("\n[*] Creator : Bilal Haider ID")
        print("[*] Tool Version : 0.0.1")
        print("[*] Tool Info : IP Information Gathering")
        print("[*] Github : https://github.com/BilalHaider-ID")
        print("[*] Copyright : GNU General Public License v3.0\n")
    elif argv[1] in ['-help','--help','-h','--h']:
        print("\n[*] -ip = [ INPUT IP ADDRESS ]")
        print("[*] -l = [ INPUT LANGUAGE ]")
        print("[*] -help = [ TOOL HELP ]")
        print("[*] -info = [ TOOL INFO ]")
        print(f"[*] use i.e : python {argv[0]} -ip 197.0.63.4")
elif len(argv)==3:
    if argv[1]=='-ip':
        ip = argv[2]
        ip_track(ip)
else:
    print(f"\n[*] use i.e : python {argv[0]} -ip TARGET IP ")
