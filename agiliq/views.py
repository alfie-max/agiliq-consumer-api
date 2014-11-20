import uuid
import requests
from agiliq import app
from flask import redirect, request, abort


client_id     = 'jpW1SVD4wdyvViEX1gb7mjTitnxnDWKLGu8BXhbrZnLB63khYm'
client_secret = 'IMKbub1eKLnkbRatVGxrMZQMYJBY8IFic14Ls82n4LY7318i2C'
redirect_uri  = 'http://127.0.0.1:5000/oauth/callback'
auth_url      = 'http://join.agiliq.com/oauth/authorize/'
token_url     = 'http://join.agiliq.com/oauth/access_token/'
state         = uuid.uuid4().get_hex()

@app.route('/')
def index():
    params = {'client_id'    : client_id,
              'state'        : state,
              'redirect_uri' : redirect_uri
    }

    req = requests.Request('GET', url=auth_url, params=params).prepare()
    return redirect(req.url)

@app.route('/oauth/callback', methods=['GET', 'POST'])
def callback():
    current_state = request.args.get('state')
    code = request.args.get('code')

    if current_state != state or not code:
        abort(403) # Forbidden

    params = {'client_id'     : client_id,
              'client_secret' : client_secret,
              'code'          : code,
              'redirect_uri'  : redirect_uri
    }
    headers = {'accept':'application/json'}

    req = requests.post(token_url, params=params, headers=headers)
    if not req.ok:
        abort(403) # Forbidden
