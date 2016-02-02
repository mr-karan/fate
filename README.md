# fate

fate is a simple CLI program which let's you browse FontAwesome icons on your terminal. 
For the icons to display properly on your system, you need to have FontAwesome fonts installed.

Example Usage : 

To browse all the icons 
fate --icon 
To narrow down you search with FontAwesome filter tags, use --filter or -f 
fate -filter
To narrow down your search with aliases tag, use --aliases or -a
fate -a
To narrow down your search with categories tag, use --category or -c
fate -c

To echo the icon name/unicode/html hex use it with -e or --echo
Example 
fate -i -e icon
or 
fate -f -e name

