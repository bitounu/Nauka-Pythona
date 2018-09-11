# -*- coding: utf-8 -*-
# Listing_6-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pierwszy program EasyGUI

import easygui
smak = easygui.buttonbox("Jaki jest TwĂłj ulubiony smak lodĂłw?",
choices = ['Waniliowe', 'Czekoladowe', 'Truskawkowe'] ) # Lista smakĂłw do wyboru
easygui.msgbox ("WybraĹ‚eĹ› " + smak)


