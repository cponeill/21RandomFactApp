# loading developer libraries
import requests, json, yaml
from flask import Flask, request
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment
from flask import send_from_directory

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

url = 'http://numbersapi.com/random/year?json'

# add routing and payment information
@app.route('/randomfact')
@payment.required(5000)
def send_random_fact():
  '''
  This simple program displays a random fact about a random year.

  Learn more about this API ---> http://numbersapi.com
  '''
  
  # Formatting the variable "url" to output JSON.
  response = requests.get(url)
  year_json = json.loads(response.text)
  
  # Return the year and text data from the json output and display it in the command line. 
  if len(year_json) == 0:
    return "There are no facts at all."
  else:
    year = year_json['number']
    text = year_json['text']
    return "Here is a random fact about the year %d\n%s" % (year, text)


@app.route('/manifest')
def docs():
  '''
  Provides the app manifest to the 21 crawler.
  '''
  with open('manifest.yaml', 'r') as f:
    manifest_yaml = yaml.load(f)
  return json.dumps(manifest_yaml)


@app.route('/client')
def client():
  '''
  Provides an example client script.
  '''
  return send_from_directory('static', 'client.py')


if __name__=='__main__':
  app.run(host='10.147.17.138', debug=True)
