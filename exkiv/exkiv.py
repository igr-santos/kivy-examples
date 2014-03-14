#!/usr/bin/env python

import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.button import Button


class ExkivApp(App):
    def build(self):
        return Button(text='Hello World.')

if __name__ in ('__android__', '__main__'):
    ExkivApp().run()
