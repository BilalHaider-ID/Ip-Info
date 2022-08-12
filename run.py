from os import *
from sys import *
from requests import *
from time import *

def ip_track(ip=""):
    try:status = get('http://ip-api.com/json/'+ip).json()['status']
    except:status = " - "
    try:country = get('http://ip-api.com/json/'+ip).json()['country']
    except:country = " - "
    try:countryCode = get('http://ip-api.com/json/'+ip).json()['countryCode']
    except:countryCode = " - "
    try:region = get('http://ip-api.com/json/'+ip).json()['region']
    except:region = " - "
    try:regionName = get('http://ip-api.com/json/'+ip).json()['regionName']
    except:regionName = " - "
    try:city = get('http://ip-api.com/json/'+ip).json()['city']
    except:city = " - "
    try:zip = get('http://ip-api.com/json/'+ip).json()['zip']
    except:zip = " - "
    try:lat = get('http://ip-api.com/json/'+ip).json()['lat']
    except:lat = " - "
    try:lon = get('http://ip-api.com/json/'+ip).json()['lon']
    except:lon = " - "
    try:timezone = get('http://ip-api.com/json/'+ip).json()['timezone']
    except:timezone = " - "
    try:isp = get('http://ip-api.com/json/'+ip).json()['isp']
    except:isp = " - "
    try:org = get('http://ip-api.com/json/'+ip).json()['org']
    except:org = " - "
    try:asa = get('http://ip-api.com/json/'+ip).json()['as']
    except:asa = " - "
    try:query = get('http://ip-api.com/json/'+ip).json()['lat']
    except:query = " - "
    print(f"\n[*] User Status : {status}")
    print(f"[*] User Country : {country}")
    print(f"[*] User CountryCode : {countryCode}")
    print(f"[*] User Region : {region}")
    print(f"[*] User RegionName : {regionName}")
    print(f"[*] User City : {city}")
    print(f"[*] User Zip : {zip}")
    print(f"[*] User Lat : {lat}")
    print(f"[*] User Lon : {lon}")
    print(f"[*] User TimeZone : {timezone}")
    print(f"[*] User ISP : {isp}")
    print(f"[*] User ORG : {org}")
    print(f"[*] User As : {asa}")
    print(f"[*] User Query : {query}\n")


if len(argv)==2:
    if argv[1] in ['-info','--info']:
        print("\n[*] Creater : Bilal Haider ID")
        print("[*] Tool Version : 0.0.1")
        print("[*] Tool Info : Ip Information Gathering")
        print("[*] Github : https://github.com/BilalHaider-ID")
        print("[*] Copyright : GNU General Public License v3.0\n")
    elif argv[1] in ['-help','--help','-h','--h']:
        print("\n[*] -ip = [ INPUT IP ADDRESS ]")
        print("[*] -l = [ INPUT LANGUAGE ]")
        print("[*] -help = [ TOOL HELP ]")
        print("[*] -info = [ TOOL INFO ]")
        print("[*] use i.e : python "+argv[0]+" -ip 197.0.63.4")
elif len(argv)==3:
    if argv[1]=='-ip':
        ip = argv[2]
        ip_track(ip)
else:
    print("\n[*] use i.e : python "+argv[0]+" -ip TARGET IP ")
