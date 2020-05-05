import json
from scripts.server.server import app


def main():
    app.run(*conf_server())
    
def conf_server():
    """ returns tuple(host, server) from the file: config.txt """

    with open('Application-VT/config.txt') as config:
        json_str = config.read()
        json_str = json.loads(json_str)
    host = json_str['server']['host']
    port = json_str['server']['port']
    return host, port


if __name__ == "__main__":
    main()
