# Listing_8-8.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# P�tla while

print "Wprowad� 3, aby kontynuowa�, lub cokolwiek innego, je�li chcesz wyj��."
jakisZnak = raw_input()

# P�tla b�dzie trwa�a tak d�ugo, jak d�ugo jakisZnak='3'
while jakisZnak == '3':
    print "Dzi�kuj� za 3. To bardzo mi�o z Twojej strony."                          # Cia�o p�tli
    print "Wprowad� 3, aby kontynuowa�, lub cokolwiek innego, je�li chcesz wyj��."  #
    jakisZnak = raw_input()                                                         #
print "To nie jest 3. Wychodz� z programu."



