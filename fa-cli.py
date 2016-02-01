#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author mr-karan

import yaml
import requests
import json
import html
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from collections import namedtuple
import argparse
parser = argparse.ArgumentParser(prog='fa-cli')
parser.add_argument('-i', '--icon', action='store_true' ,help='Enter icon name')
parser.add_argument('-f', '--filter', action='store_true' ,help='Filter Font awesome icons')
parser.add_argument('-a', '--aliases', action='store_true' ,help='Aliases')
parser.add_argument('-c', '--category', action='store_true'  ,help='Category Icons')
args = parser.parse_args()

def clean(a):
    for i in a:
        try:

            if (i['aliases']):
                continue

        except KeyError:
            i['aliases']=''
    for i in a:
        try:

            if (i['filter']):
                continue

        except KeyError:
            i['filter']=''     
    return a 

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

def auto_complete(p_list):
    search_by_filter = [p_list[i][1] for i in range(len(p_list)) if (p_list[i][1] is not None)]
    search_by_aliases = [p_list[i][4] for i in range(len(p_list)) if (p_list[i][4] is not None)]
    search_by_icon = [p_list[i][2] for i in range(len(p_list)) if (p_list[i][2] is not None)]
    search_by_category = [p_list[i][0] for i in range(len(p_list)) if (p_list[i][0] is not None)]
    f_completer = WordCompleter(list(set([k for i in search_by_filter for k in i ])))
    a_completer = WordCompleter(list(set([k for i in search_by_aliases for k in i ])))
    i_completer = WordCompleter(search_by_icon)
    c_completer = WordCompleter(list(set([k.lower() for i in search_by_category for k in i ])))
    textf = prompt('Search By Filter: ', completer=f_completer)
    texta = prompt('Search by Aliases: ', completer=a_completer)
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    textc = prompt('Search by Category: ', completer=c_completer)
    #print(textf)
    #print(texta)
    #print(texti)
    #print(textc)
    #html_entity ='&#x'+k['unicode']
    #print(html_entity)
    #print(k['name'])
    #print(html.unescape(html_entity))

#auto_complete(p_list)

#if args.icon:
#    auto_complete(icon_list)
if args.filter:
    search_by_filter = [p_list[i][1] for i in range(len(p_list)) if (p_list[i][1] is not None)]
    f_completer = WordCompleter(list(set([k for i in search_by_filter for k in i ])))
    textf = prompt('Search By Filter: ', completer=f_completer)
    give_id = {p_list[i][2]:p_list[i][3] for i in range(len(p_list)) if (p_list[i][1] is not None) and (textf in p_list[i][1])}
    for i in list(give_id.keys()):
        print(i)
    i_completer = WordCompleter(list(give_id.keys()))
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    msg = '''Icon Details
    Name : {0}
    Unicode : {1}
    HTML Hex :  {2}
    Icon :{3}

    '''.format('fa-'+texti,give_id[texti],'&#x'+give_id[texti],html.unescape('&#x'+give_id[texti]))
    print(msg)
        
if args.aliases:
    auto_complete(p_list)
if args.category:
    auto_complete(p_list)
    