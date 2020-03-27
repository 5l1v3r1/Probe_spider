import json
import requests

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def SubDomain(host, port):
    print ( W + '[+]' + G + 'Fetching Subdomains of Target...' + '\n')
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {'apikey':'1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}

    response = requests.get(url, params=params)

    subdomains = response.json()

    for x in subdomains['domain_siblings']:
        print(x)
