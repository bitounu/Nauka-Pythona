# Listing_8-8.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pętla while

print "Wprowadź 3, aby kontynuować, lub cokolwiek innego, jeśli chcesz wyjść."
jakisZnak = raw_input()

# Pętla będzie trwała tak długo, jak długo jakisZnak='3'
while jakisZnak == '3':
    print "Dziękuję za 3. To bardzo miło z Twojej strony."                          # Ciało pętli
    print "Wprowadź 3, aby kontynuować, lub cokolwiek innego, jeśli chcesz wyjść."  #
    jakisZnak = raw_input()                                                         #
print "To nie jest 3. Wychodzę z programu."



