# fate

>fate is a simple CLI program which let's you browse FontAwesome icons on your terminal. 
Note : Python3+ only.

Install Instructions : 
`pip install fate`
or 
`pip install git+https://github.com/mr-karan/fate.git`

[![asciicast](https://asciinema.org/a/9oyqtsd9r6xh3ppryiy0yu14r.png)](https://asciinema.org/a/9oyqtsd9r6xh3ppryiy0yu14r)

For the icons to display properly on your system, you need to have FontAwesome fonts installed.
Grab the otf files from [here](https://fortawesome.github.io/Font-Awesome/)
You need to install this font on your system for icons to be rendered properly.

For Windows user : 
 - [ ] Since PyYAML isn't actively maintained, you need to grab it manaully from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyyaml)
 - [ ] If you are using, cmd god bless you. Change the character map using chcp 65001

###Avilable commands : 
#### To browse all the icons 
`fate --icon `

![icon](screenshots/icon.png)
#### To narrow down you search with FontAwesome filter tags, use --filter or -f
`fate -filter`

![icon](screenshots/filter.png)
#### To narrow down your search with aliases tag, use --aliases or -a
`fate --aliases`

![icon](screenshots/aliases.png)
#### To narrow down your search with categories tag, use --category or -c
`fate --category`

![icon](screenshots/category.png)
#### To echo the icon name/unicode/html hex use it with -e or --echo
#####Example : 
`fate -i -e icon`

![icon](screenshots/echo.png)

### What's with the name ? 

Well, 'F'ont'A'wesome on 'Te'rminal = "fate" :)
Credits to my good friend [@Kush](https://twitter.com/BurstDragon)

### License
