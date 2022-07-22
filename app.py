import os
from requests import get
from flask import Flask, Response

app = Flask(__name__)

proxy_url = os.environ['TARGET_URL']


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    content = get(f'{proxy_url}/{path}').content
    print(content)
    return Response(content, mimetype="application/json", headers={
        "Access-Control-Allow-Origin": "*",
        "Cache-Control": "max-age=3600"
    })


if __name__ == '__main__':
    app.run(
        host=os.environ.get('ADDRESS', '0.0.0.0'),
        port=int(os.environ['PORT']),
        debug=os.environ.get('VERBOSE', 'false') == 'true')
