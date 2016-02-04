# fate

## fate is a simple CLI program which let's you browse FontAwesome icons on your terminal. 

Install Instructions : 
`pip install fate`
or 
`pip install git+https://github.com/mr-karan/fate.git`

For the icons to display properly on your system, you need to have FontAwesome fonts installed.
For Windows user : 
 - [ ] Since PyYAML isn't actively maintained, you need to grab it manaully from
 - [ ] If you are using, cmd god bless you. Change the character map using chcp 65001

###Avilable commands : 
#### To browse all the icons 
`fate --icon `
#### To narrow down you search with FontAwesome filter tags, use --filter or -f
`fate -filter`
#### To narrow down your search with aliases tag, use --aliases or -a
`fate --aliases`
#### To narrow down your search with categories tag, use --category or -c
`fate --category`
#### To echo the icon name/unicode/html hex use it with -e or --echo
#####Example : 
`fate -i -e icon`
`fate -f -e name`

### What's with the name ? 

Well, 'F'ont'A'wesome on 'Te'rminal = "fate" :)

