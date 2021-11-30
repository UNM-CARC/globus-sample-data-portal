#!/usr/bin/env python

import ssl
from service import app

if __name__ == '__main__':
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain('./ssl/server.crt', './ssl/server.key')
    app.run(host='0.0.0.0', port=5100, debug=True, ssl_context=ctx)
