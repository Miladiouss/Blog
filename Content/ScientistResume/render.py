#! /usr/bin/env python

import yaml
from jinja2 import Environment, FileSystemLoader
from munch import Munch
from pathlib import Path

here = Path(__file__).parent
print(here)
contentPath = here / "content.yaml"
with contentPath.open("r") as stream:
    content = yaml.safe_load(stream)
    content = Munch.fromDict(content)

env = Environment(loader=FileSystemLoader(here))
tempPath = here / 'page-template.html'
rendered = env.get_template('page-template.html', here).render(content)

pagePath = here / 'page.html'
with pagePath.open('w') as stream:
    stream.write(rendered)
