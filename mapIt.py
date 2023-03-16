"""
    First you need to figure out what URL to use for a given street address. 
When you load http://maps.google.com/ in the browser and search for an 
address, the URL in the address bar looks something like this: https://
www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/
data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8.
The address is in the URL, but there's a lot of additional text there as 
well. Websites often add extra data to URLs to help track visitors or customize sites. But if you try just going to https://www.google.com/maps/place/870+
Valencia+St+San+Francisco+CA/, you'll find that it still brings up the correct page. So your program can be set to open a web browser to 'https://
www.google.com/maps/place/your_address_string' (where your_address_string is 
the address you want to map)
"""
#! python
# mapIt.py - launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, clipboard as cp
if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = cp.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)