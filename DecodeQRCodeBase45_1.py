#! /usr/bin/env python3
import json
import sys
import zlib

import base45
import cbor2
from cose.messages import CoseMessage

payload = sys.argv[1][4:]
print("decoding payload: "+ payload)

# décode Base45 (retire HC1: prefix)
decoded = base45.b45decode(payload)

# decompress avec zlib
decompressed = zlib.decompress(decoded)
# décode COSE message (sans verifier la signature)
cose = CoseMessage.decode(decompressed)
# décode le payload CBOR encodé et le print au format json
print(json.dumps(cbor2.loads(cose.payload), indent=2))
