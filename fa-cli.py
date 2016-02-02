#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
fate CLI
    Copyright (C) 2016 Karan Sharma
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

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
parser = argparse.ArgumentParser(prog='fa-cli', description='FontAwesome CLI')
parser.add_argument('-i', '--icon', action='store_true', help='Enter icon name')
parser.add_argument('-f', '--filter', action='store_true', help='Filter Font awesome icons')
parser.add_argument('-a', '--aliases', action='store_true', help='Aliases')
parser.add_argument('-c', '--category', action='store_true', help='Category Icons')
parser.add_argument('-e','--echo', type=str, nargs=1, action='store', help='Copies the data to your clipboard', metavar = ("name/unicode/icon"))
args = parser.parse_args()

# Outputs the icon details to the user. Also copies the data to clipboard if -e [data] is present.


def message(give_id, text):
    name = 'fa-'+text
    uni = give_id[text]
    hexhtml = '&#x'+give_id[text]
    icon = html.unescape('&#x'+give_id[text])

    if args.echo:
        if args.echo[0] == 'unicode':
            pyperclip.copy(give_id[text])
        if args.echo[0] == 'name':
            pyperclip.copy('fa-'+text)
        if args.echo[0] == 'icon':
            pyperclip.copy(html.unescape('&#x'+give_id[text]))
    return '''Icon Details
    Name : {0}
    Unicode : {1}
    HTML Hex :  {2}
    Icon : {3}

    '''.format(name, uni, hexhtml, icon)

if __name__ == '__main__':
    # Maintain a cache so that everytime it doesn't need to request the source file.
    try:
        with open('.fa_cache', 'r') as cache_file:
            icon_data = json.load(cache_file)
    except FileNotFoundError:
        yaml_file = requests.get("https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml").text
        # clean() is defined in helpers. The source file had inconsistencies like missing fields.
        clean_source = clean((yaml.load(yaml_file))['icons'])
        # Used to store IconData in a namedtupe data structure.
        data = namedtuple('IconData', 'categories filter id unicode aliases')

        icon_data = [data(i['categories'], i['filter'], i['id'], i['unicode'], i['aliases']) for i in clean_source]
        with open('.fa_cache', 'w') as the_file:
            the_file.write(json.dumps(icon_data, indent=2))

    if args.icon:
        search_by_id = icon_list(icon_data)
        give_id = give_id_unicode(icon_data)
        i_completer = WordCompleter(search_by_id)
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id, texti))

    if args.filter:
        # Second parameter(1) is the positon of the attribute in IconData()
        search_by_filter = icon_list(icon_data, 1)
        # Appends all the categories of FA and set() to remove duplicate entries filling up
        f_completer = WordCompleter(list(set([k for i in search_by_filter for k in i])))
        textf = prompt('Search By Filter: ', completer=f_completer)
        # Gives the list of icons which matched that category
        give_id = give_id_unicode(icon_data, textf, 1)
        # Function in helpers, prints the icon list to output stream
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id, texti))

    if args.aliases:
        search_by_aliases = icon_list(icon_data, 4)
        f_completer = WordCompleter(list(set([k for i in search_by_aliases for k in i])))
        textf = prompt('Search By Aliases: ', completer=f_completer)
        give_id = give_id_unicode(icon_data, textf, 4)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id, texti))

    if args.category:
        # 0 because the position of category in IconData() is the first one.
        search_by_category = icon_list(icon_data, 0)
        f_completer = WordCompleter(list(set([k for i in search_by_category for k in i])))
        textf = prompt('Search By Category: ', completer=f_completer)
        give_id = give_id_unicode(icon_data, textf, 0)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id, texti))
