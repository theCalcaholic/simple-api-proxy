import os
from urllib.parse import unquote_plus
from requests import get
from flask import Flask, Response, request

app = Flask(__name__)

proxy_url = os.environ['TARGET_URL']


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    query = request.query_string.decode('utf8')
    query = "" if len(query) == 0 else f"?{query}"
    content = get(f'{proxy_url}/{path}{query}').content
    return Response(content, mimetype="application/json", headers={
        "Access-Control-Allow-Origin": "*"
    })


if __name__ == '__main__':
    app.run(
        host=os.environ.get('ADDRESS', '0.0.0.0'),
        port=int(os.environ['PORT']),
        debug=os.environ.get('VERBOSE', 'false') == 'true')
