#!/usr/lib/python

import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

from sleekxmpp import ClientXMPP

class AccountDetailsForm(AnchorLayout):
    server_input = ObjectProperty()
    username_input = ObjectProperty()
    password_input = ObjectProperty()

    def login(self):
        username = "%s@%s" % (self.username_input.text, self.server_input.text)
        password = self.password_input.text
	
	app = Exkiv.get_running_app()
        app.connect_to_server(username, password)
        print app.xmpp.client_roster.keys()
        app.xmpp.disconnect()

class Exkiv(App):
    def connect_to_server(self, username, password):
        self.xmpp = ClientXMPP(username, password)
        self.xmpp.connect()
        self.xmpp.process()
        self.xmpp.send_presence()
        self.xmpp.get_roster()

Exkiv().run()
