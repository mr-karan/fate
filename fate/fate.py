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
from .helpers import *
parser = argparse.ArgumentParser(prog='fate', description='FontAwesome on Terminal')
parser.add_argument('-i', '--icon', action='store_true', help='Enter icon name')
parser.add_argument('-f', '--filter', action='store_true', help='Filter Font awesome icons')
parser.add_argument('-a', '--aliases', action='store_true', help='Aliases')
parser.add_argument('-c', '--category', action='store_true', help='Category Icons')
parser.add_argument('-e','--echo', type=str, nargs=1, action='store', help='Copies the data to your clipboard', metavar = ("name/unicode/icon"))
args = parser.parse_args()


def main():
    # Output the icon details to the user
    def message(give_id, text):
        try:
            if give_id[text]:
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
        except KeyError:
            print('Invalid name')
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
        # Appends all the categories of FA and set() is used to remove duplicate entries filling up
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
        search_by_category = icon_list(icon_data, 0)
        f_completer = WordCompleter(list(set([k for i in search_by_category for k in i])))
        textf = prompt('Search By Category: ', completer=f_completer)
        give_id = give_id_unicode(icon_data, textf, 0)
        icon_output(list(give_id.keys()))
        i_completer = WordCompleter(list(give_id.keys()))
        texti = prompt('Enter Icon Name: ', completer=i_completer)
        print(message(give_id, texti))


if __name__ == '__main__':
    main()