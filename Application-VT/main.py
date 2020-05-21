import json
from scripts.server.server import app
import sys


def main():
    print(conf_server())
    app.run(*conf_server())


def conf_server() -> tuple:
    """ returns tuple(host, server) from the file: config.txt """
    with open('Application-VT/config.txt') as config:
        json_str = config.read()
        json_str = json.loads(json_str)

    host = json_str['server']['host']
    port = json_str['server']['port']
    return host, port


if __name__ == "__main__":
        main()

