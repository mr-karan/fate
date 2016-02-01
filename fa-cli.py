#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author : mr-karan (Karan Sharma)
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

def give_id_unicode(p_list,*text):
    if text:
        id_unicode = {p_list[i][2]:p_list[i][3] for i in range(len(p_list)) if (p_list[i][text[1]] is not None) and (text[0] in p_list[i][text[1]])}
    else:
        id_unicode = {p_list[i][2]:p_list[i][3] for i in range(len(p_list))}
    return id_unicode

def message(give_id,text):
    return '''Icon Details
    Name : {0}
    Unicode : {1}
    HTML Hex :  {2}
    Icon :{3}

    '''.format('fa-'+text,give_id[text],'&#x'+give_id[text],html.unescape('&#x'+give_id[text]))
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

if args.icon:
    search_by_id=[p_list[i][2] for i in range(len(p_list))]
    give_id = give_id_unicode(p_list)
    i_completer = WordCompleter(search_by_id)
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    print(message(give_id,texti))
    
if args.filter:
    search_by_filter = [p_list[i][1] for i in range(len(p_list)) if (p_list[i][1] is not None)]
    f_completer = WordCompleter(list(set([k for i in search_by_filter for k in i ])))
    textf = prompt('Search By Filter: ', completer=f_completer)
    give_id = give_id_unicode(p_list,textf,1)
    for i in list(give_id.keys()):
        print(i)
    i_completer = WordCompleter(list(give_id.keys()))
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    print(message(give_id,texti))

        
if args.aliases:
    search_by_aliases = [p_list[i][4] for i in range(len(p_list)) if (p_list[i][4] is not None)]
    f_completer = WordCompleter(list(set([k for i in search_by_aliases for k in i ])))
    textf = prompt('Search By Aliases: ', completer=f_completer)
    give_id = give_id_unicode(p_list,textf,4)
    for i in list(give_id.keys()):
        print(i)
    i_completer = WordCompleter(list(give_id.keys()))
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    print(message(give_id,texti))

if args.category:
    search_by_category = [p_list[i][0] for i in range(len(p_list)) if (p_list[i][0] is not None)]
    f_completer = WordCompleter(list(set([k for i in search_by_category for k in i ])))
    textf = prompt('Search By Category: ', completer=f_completer)
    give_id = give_id_unicode(p_list,textf,0)
    for i in list(give_id.keys()):
        print(i)
    i_completer = WordCompleter(list(give_id.keys()))
    texti = prompt('Enter Icon Name: ', completer=i_completer)
    print(message(give_id,texti))

    
    