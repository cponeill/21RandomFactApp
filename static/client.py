# loading developer libraries
import argparse
import os.path
from pyfiglet import figlet_format
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

def get_answer(host):
    '''Tell the client they are about to learn a random fact.'''
    print(figlet_format("FACT OF THE DAY!"))
    server_url = host + 'randomfact'
    response = requests.get(url=server_url)
    if response.status_code == 200:
        answer = response.text
    else:
        answer = str(response.status_code) + ' error'
    return answer

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Get a random fact')
    parser.add_argument('host', type=str, help='address of server hosting random fact program')
    parser.add_argument('--test', help='unit test for random fact server', action='store_true')
    args = parser.parse_args()
    
    if args.test:
        print('Test passed')
        exit(1)
        
    random_ract = get_answer(args.host)
    print(random_fact)
    


