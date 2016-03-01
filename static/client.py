# loading developer libraries
from pyfiglet import figlet_format
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

#server_url = 'http://localhost:5000/'
server_url = 'http://10.147.17.138:5000/'

def get_answer():
    '''Tell the client they are about to learn a random fact.'''
    print(figlet_format("FACT OF THE DAY!"))
    response = requests.get(url=server_url+'randomfact')
    answer = response.text
    print(answer)

if __name__=='__main__':
    get_answer()

