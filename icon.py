  #!/usr/bin/python
  # -*- coding: UTF-8 -*-

import yaml
import requests
import json
import html
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
import argparse
#parser = argparse.ArgumentParser(prog='fa-cli')
#parser.add_argument('-i', '--icon', type=auto_complete() ,help='Enter fontawesome icon name')
#args = parser.parse_args()

try:
    with open('.fa_cache.json','r') as the_json:
        aa = json.load(the_json)
        
except FileNotFoundError:
    yaml_file = requests.get("https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml").text
    icon_yaml = (yaml.load(yaml_file))['icons']
    name_unicode ={}
    for i in icon_yaml:
        name_unicode[i['id']]=i['unicode']
    aa = name_unicode
    with open('.fa_cache.json','w') as the_file:
        the_file.write(json.dumps(name_unicode,indent=2))
#user = input(">")
#choices = suggestions(user,aa.keys()) 
#choices_name = [i[0] for i in choices]

def auto_complete():
    icon_completer = WordCompleter(aa.keys())
    text = prompt('Enter Icon Name: ', completer=icon_completer)
    html_entity ='&#x'+aa[text]
    print(html_entity)
    print(aa[text])
    print(html.unescape(html_entity))

auto_complete()