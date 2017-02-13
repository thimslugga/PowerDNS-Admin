#!/usr/bin/env python

from app import app
from config import BIND_ADDRESS, PORT, DEBUG

if __name__ == '__main__':
    app.run(host=BIND_ADDRESS, port=PORT, debug=DEBUG)
