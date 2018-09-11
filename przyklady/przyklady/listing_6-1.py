# -*- coding: utf-8 -*-
# Listing_6-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pierwszy program EasyGUI

import easygui
smak = easygui.buttonbox("Jaki jest Twój ulubiony smak lodów?",
choices = ['Waniliowe', 'Czekoladowe', 'Truskawkowe'] ) # Lista smaków do wyboru
easygui.msgbox ("Wybrałeś " + smak)


