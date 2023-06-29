from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def webserver():
    if request.method == 'GET':
        return f"""
          <html>
          <head>
              <p>$##$$Hello World$##$</p>
          </head>
          </html>
          """


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
