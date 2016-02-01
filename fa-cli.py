  #!/usr/bin/python
  # -*- coding: UTF-8 -*-
import yaml
import requests
import json
import html
import argparse
import pyperclip
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from collections import namedtuple
from helpers import *
parser = argparse.ArgumentParser(prog='fa-cli',description='FontAwesome CLI')
parser.add_argument('-i', '--icon', action='store_true' ,help='Enter icon name')
parser.add_argument('-f', '--filter', action='store_true' ,help='Filter Font awesome icons')
parser.add_argument('-a', '--aliases', action='store_true' ,help='Aliases')
parser.add_argument('-c', '--category', action='store_true'  ,help='Category Icons')
parser.add_argument('-o','--output',type=str,nargs=1, action='store',help='Copies the data to your clipboard', metavar = ("name / unicode /icon"))
args = parser.parse_args()

def message(give_id,text):
    if args.output:
        if args.output[0] =='unicode':
            pyperclip.copy(give_id[text])
        if args.output[0] =='name':
            pyperclip.copy('fa-'+text)
        if args.output[0] =='icon':
            pyperclip.copy(html.unescape('&#x'+give_id[text]))
    return '''Icon Details
    Name : {0}
    Unicode : {1}
    HTML Hex :  {2}
    Icon :{3}

    '''.format('fa-'+text,give_id[text],'&#x'+give_id[text],html.unescape('&#x'+give_id[text]))

if __name__ =='__main__':
    try:
        with open('.fa_cache','r') as the_json:
            p_list = json.load(the_json)
            
    except FileNotFoundError:
        yaml_file = requests.get("https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml").text
        a = clean((yaml.load(yaml_file))['icons'])
        data=namedtuple('IconData','categories filter id unicode aliases')
        p_list = [data(i['categories'],i['filter'],i['id'],i['unicode'],i['aliases']) for i in a]
        with open('.fa_cache','w') as the_file:
            the_file.write(json.dumps(p_list,indent=2))

    if args.icon:
        search_by_id=icon_list(p_list)
        give_id = give_id_unicode(p_list)
        i_completer = WordCompleter(search_by_id)
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id,texti))


        
    if args.filter:
        search_by_filter = icon_list(p_list,1)
        f_completer = WordCompleter(list(set([k for i in search_by_filter for k in i ])))
        textf = prompt('Search By Filter: ', completer=f_completer)
        give_id = give_id_unicode(p_list,textf,1)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id,texti))

            
    if args.aliases:
        search_by_aliases = icon_list(p_list,4)
        f_completer = WordCompleter(list(set([k for i in search_by_aliases for k in i ])))
        textf = prompt('Search By Aliases: ', completer=f_completer)
        give_id = give_id_unicode(p_list,textf,4)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id,texti))

    if args.category:
        search_by_category = icon_list(p_list,0)
        f_completer = WordCompleter(list(set([k for i in search_by_category for k in i ])))
        textf = prompt('Search By Category: ', completer=f_completer)
        give_id = give_id_unicode(p_list,textf,0)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id,texti))

    
