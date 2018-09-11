# -*- coding: utf-8 -*-
# Listing_6-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# EasyGUI - wybór domyślnej wartości za pomocą funkcji enterbox()

import easygui
smak = easygui.enterbox("Jaki jest Twój ulubiony smak lodów?",
                       default = 'Waniliowe')
easygui.msgbox ("Wybrałeś " + smak)



