# loading developer libraries
from pyfiglet import figlet_format
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

server_url = 'http://localhost:5000/'
#server_url = 'http://10.244.189.126:5000/'

def get_answer():
    '''Tell the client they are about to learn a random fact.'''
    print(figlet_format("FACT OF THE DAY!"))
    response = requests.get(url=server_url+'randomfact')
    if response.status_code == 200:
        answer = response.text
    else:
        answer = str(response.status_code) + ' error'
    print(answer)

if __name__=='__main__':
    get_answer()


