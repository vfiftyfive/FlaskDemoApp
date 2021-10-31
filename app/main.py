import pyfiglet
import os
from flask import Flask

app = Flask(__name__)
path = '/mnt/message/text'

@app.route("/")
def main():
    message = None
    
    try:
        with open(path, 'r') as file:
            message = file.read().replace('\n', '')
    except FileNotFoundError:
        pass
        
    if message is not None:
        return pyfiglet.figlet_format(message)
    if os.getenv("OWNER") is not None:
        message = os.getenv("OWNER") + " Was Here!!! "
    else:
        message = os.getenv("MESSAGE", "no message specified")
    
    return pyfiglet.figlet_format(message)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)