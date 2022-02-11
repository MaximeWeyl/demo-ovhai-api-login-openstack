import json
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

def get_config():
    config = json.load(open('config.json'))
    return config

def connect_regionnal(config):
    client_id = config['clientId']
    client_secret = config['clientSecret']
    username = config['userOpenStack']
    password = config['passwordOpenStack']
    token_url = config['regionalTokenUrl']

    session = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
    session.fetch_token(
        token_url=token_url,
        username=username, password=password,
        client_id=client_id,
        client_secret=client_secret
    )
    return session
