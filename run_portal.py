#!/usr/bin/env python

import ssl
from portal import app

if __name__ == '__main__':
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain('./ssl/server.crt', './ssl/server.key')
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=ctx)
