from txtmarker.factory import Factory
from txtmarker import base
import sys
import argparse
import re

if len(sys.argv) <= 3:
    print("{} infile outfile text|regex [text|regex ...]".format(sys.argv[0]))
    sys.exit(0)

#infile=sys.argv[1]
#outfile=sys.argv[2]
#text=sys.argv[3]

parser = argparse.ArgumentParser(                                                                               # noqa
    description='text highlighter for screenplays', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('infile', help='input pdf.')
parser.add_argument('outfile', help='output pdf.')
parser.add_argument('pattern', help='text|pattern to search.')
parser.add_argument('-i', '--ignorecase', action='store_true', help='search case insensitive.')
parser.add_argument('-m', '--multiline', action='store_true', help='seaerch multiline.')
parser.add_argument('-c', '--color', choices=['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'bronze', None], default=None, help='highlight color. (default=None (random color)')
app_args = parser.parse_args()

colors = {name:index for index,name in enumerate(["red", "blue", "yellow", "green", "purple", "orange", "bronze"])}

reflags = 0

if app_args.ignorecase:
    reflags |= re.IGNORECASE
if app_args.multiline:
    reflags |= re.MULTILINE
if app_args.color:
    color_index = colors[app_args.color]
else:
    color_index = None


highlighter = Factory.create("pdf")

highlighter.highlight(app_args.infile, app_args.outfile, [(None, app_args.pattern)], color_index, reflags)


