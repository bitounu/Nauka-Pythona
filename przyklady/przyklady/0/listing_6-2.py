# -*- coding: utf-8 -*-
# Listing_6-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# EasyGUI - wybieranie smaku za pomoca funkcji choicebox()

import easygui
smak = easygui.choicebox("Jaki jest TwĂłj ulubiony smak lodĂłw?",
choices = ['Waniliowe', 'Czekoladowe', 'Truskawkowe'] )
easygui.msgbox ("WybraĹ‚eĹ› " + smak)

