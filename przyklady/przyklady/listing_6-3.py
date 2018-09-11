# -*- coding: utf-8 -*-
# Listing_6-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# EasyGUI - wybieranie smaku za pomoca funkcji enterbox()

import easygui
smak = easygui.enterbox("Jaki jest Twój ulubiony smak lodów?")
easygui.msgbox ("Wybrałeś " + smak)


