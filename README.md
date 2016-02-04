# fate
[![Github All Releases](https://img.shields.io/github/downloads/mr-karan/fate/total.svg)]()
[![version](https://img.shields.io/pypi/v/fate.svg)](https://pypi.python.org/pypi/fate/)
[![supported](https://img.shields.io/pypi/pyversions/fate.svg)](https://pypi.python.org/pypi/fate/)
[![Twitter](https://img.shields.io/twitter/url/https/pypi.python.org/pypi/fate.svg?style=social?style=flat-square)](https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/mr-karan/fate/master/LICENSE)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)
>fate is a simple CLI program which let's you browse FontAwesome icons on your terminal. 
Note : Python3+ only.

Install Instructions : 
`pip install fate`
or 
`pip install git+https://github.com/mr-karan/fate.git`

[![asciicast](https://asciinema.org/a/9oyqtsd9r6xh3ppryiy0yu14r.png)](https://asciinema.org/a/9oyqtsd9r6xh3ppryiy0yu14r)

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
#### To echo the icon `[name/ unicode/ html]` hex use it with -e or --echo
#####Example : 
`fate -i -e name`

![icon](screenshots/echo.png)

### What's with the name ? 

Well, 'F'ont'A'wesome on 'Te'rminal = "fate" :)
Credits to my good friend [@Kush](https://twitter.com/BurstDragon)

For the icons to display properly on your system, you need to have FontAwesome fonts installed.
Grab the otf files from [here](https://fortawesome.github.io/Font-Awesome/)
You will need to install this font on your system for icons to be rendered properly.

For Windows users : 
 - pip install would most likely fail to install `pyyaml`, since `PyYAML` isn't actively maintained. You need to grab it manaully from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyyaml)
 - If you are using `cmd` god bless you. Change the character map using `chcp 65001`. Check [here](http://stackoverflow.com/questions/14109024/how-to-make-unicode-charset-in-cmd-exe-by-default) for additional instructions.

### License
> MIT © Karan Sharma 

> [LICENSE included here](LICENSE)
