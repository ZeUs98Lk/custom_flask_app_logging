from flask import Flask
import logging

app = Flask(__name__)

# Configure logging to write to a file
handler = logging.FileHandler('app.log', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info("There was an HTTP request.")
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)