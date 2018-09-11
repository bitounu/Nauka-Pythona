# -*- coding: utf-8 -*-
# Listing_6-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# EasyGUI - wybĂłr domyĹ›lnej wartoĹ›ci za pomocÄ… funkcji enterbox()

import easygui
smak = easygui.enterbox("Jaki jest TwĂłj ulubiony smak lodĂłw?",
                       default = 'Waniliowe')
easygui.msgbox ("WybraĹ‚eĹ› " + smak)



