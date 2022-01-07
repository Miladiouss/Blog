#!/usr/bin/env python
import yaml
from jinja2 import Environment, FileSystemLoader
from munch import Munch

with open("content.yaml", "r") as stream:
    content = yaml.safe_load(stream)
    content = Munch.fromDict(content)

env = Environment(loader=FileSystemLoader(''))
rendered = env.get_template('page-template.html').render(content)

with open('page.html', 'w') as stream:
    stream.write(rendered)
