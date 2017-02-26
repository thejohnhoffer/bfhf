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
    args = parser.parse_args()
    root = args.directory

    all_dir = sorted(os.listdir(root))
    fnames = [f for f in all_dir if f not in EXCLUDED]

    footer = ''
    footpath = os.path.join(root, 'footer.html')
    if os.path.exists(footpath):
        with open(footpath,'r') as footml:
            footer = footml.read()

    form = Template(INDEX_TEMPLATE)
    details = {
        'title': root,
        'names': fnames,
        'footer': footer
    }

    output = os.path.join(root, 'index.html')
    with open(output,'w') as outml:
        final = form.render(**details)
        outml.write(final)


if __name__ == '__main__':
    main()
