# fate
[![version](https://img.shields.io/pypi/v/fate.svg)](https://pypi.python.org/pypi/fate/)
[![supported](https://img.shields.io/pypi/pyversions/fate.svg)](https://pypi.python.org/pypi/fate/)
[![Twitter](https://img.shields.io/twitter/url/https/pypi.python.org/pypi/fate.svg?style=social?style=flat-square)](https://twitter.com/intent/tweet?text=FontAwesome on Terminal:&url=https://github.com/mr-karan/fate)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/mr-karan/fate/master/LICENSE)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)
>fate is a simple CLI program which let's you browse FontAwesome icons on your terminal. 
Note : Python3+ only.

### Installation : 

> `pip install fate`

[![asciicast](https://asciinema.org/a/35509.png)](https://asciinema.org/a/35509)

###Avilable commands : 
#### To browse all the icons.

`fate --icon `

![icon](screenshots/icon.png)

![icon](screenshots/auto.png)

#### To narrow down you search with FontAwesome filter tags, use --filter or -f
`fate -filter`

![icon](screenshots/filter.png)
##### To narrow down your search with aliases tag, use --aliases or -a
`fate --aliases`

![icon](screenshots/aliases.png)
##### To narrow down your search with categories tag, use --category or -c
`fate --category`

![icon](screenshots/category.png)
##### To echo the icon `[name/ unicode/ html]` hex use it with -e or --echo

> Example : 

`fate -i -e name`

![icon](screenshots/echo.png)

### What's with the name ? 

Well, 'F'ont'A'wesome on 'Te'rminal = "fate" :)
Credits to my good friend [@Kush](https://twitter.com/BurstDragon)

### Facing problems with Font Rendering ?
For the icons to display properly on your system, you need to have FontAwesome fonts installed.
Grab the otf files from [here](https://fortawesome.github.io/Font-Awesome/)
You will need to install this font on your system for icons to be rendered properly.
Instructions [here](http://askubuntu.com/questions/191778/how-to-install-many-font-files-fast-and-easy)
[Update](http://askubuntu.com/questions/605986/how-can-i-upgrade-gnome-terminal-on-ubuntu-14-04-lts) your gnome-terminal
Also if you are still not able to get the fonts, you may have to perform the step listed as : 
To use it in Linux within gnome-terminal you need to put `FontAwesome.otf`
inside your `~/.fonts/` folder on Linux. And create a
`~/.config/fontconfig/fonts.conf` file with the following content:

    <?xml version='1.0'?>
    <!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
    <fontconfig>
    <!-- Font families -->
    <alias>
      <family>serif</family>
      <prefer>
        <family>DejaVu Serif</family>
        <family>Android Emoji</family>
        <family>Symbola</family>
      </prefer>
    </alias>
    <alias>
      <family>sans-serif</family>
      <prefer>
        <family>DejaVu Sans</family>
        <family>Android Emoji</family>
        <family>Symbola</family>
      </prefer>
    </alias>
    <alias>
      <family>monospace</family>
      <prefer>
        <family>Ubuntu Mono</family> <!-- change this to your prefered monospace font if you like -->
        <family>DejaVu Sans Mono</family>
        <family>Android Emoji</family> <!-- put the Symbola line before this if you prefer Symbola to Android Emoji -->
        <family>Symbola</family>
        <family>FontAwesome</family>
      </prefer>
    </alias>
    </fontconfig>
[SOurce] https://github.com/AnthonyDiGirolamo/els/blob/master/README.markdown)

For Windows users : 
 - pip install would most likely fail to install `pyyaml`, since `PyYAML` isn't actively maintained. You need to grab it manaully from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyyaml)
 - If you are using `cmd` god bless you. Change the character map using `chcp 65001`. Check [here](http://stackoverflow.com/questions/14109024/how-to-make-unicode-charset-in-cmd-exe-by-default) for additional instructions.

### License
> MIT © Karan Sharma 

> [LICENSE included here](LICENSE)
