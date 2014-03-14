#!/usr/bin/env python

import sys
import sleekxmpp

xmpp = sleekxmpp.ClientXMPP(sys.argv[1], sys.argv[2])

xmpp.connect()
xmpp.process()
xmpp.send_presence()
xmpp.get_roster()
print xmpp.client_roster.keys()
xmpp.disconnect()
