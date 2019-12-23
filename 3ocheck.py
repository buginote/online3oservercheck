import requests
import os

serverlist = "https://console.online.net/en/order/server"
html = requests.get(serverlist).text

if "2.99 €" in html:
    os.system('curl https://api.day.app/LEw9aChjAv6pWZCmyc6LWa/Warning/3o_available!!!')