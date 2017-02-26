""" Build index from directory listing
"""

INDEX_TEMPLATE = r"""
<html>
<body>
<h2>${title}</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}<a></li>
% endfor
</p>
${footer}
</body>
</html>
"""

EXCLUDED = ['index.html']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--footer")
    args = parser.parse_args()
    footer = ''
    if args.footer:
        with open(parser.footer,'r') as footml:
            footer = footml.read()
    all_dir = sorted(os.listdir(args.directory))
    fnames = [f for f in all_dir if f not in EXCLUDED]
    title = os.path.basename(args.directory)

    form = Template(INDEX_TEMPLATE)
    details = {
        'names': fnames,
        'title': title,
        'footer': footer
    }
    print(form.render(**details))


if __name__ == '__main__':
    main()
