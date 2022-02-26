from ipsedixit import Generator, parse_args
import sys

if (sys.argv[1][0] != '-') and (len(sys.argv) > 2) and (sys.argv[2][0] != '-'):
    bpath = sys.argv[2]
    sys.argv.pop(2)
    if (bpath not in ('caesar', 'tacitus')):
        with open(bpath, 'r') as f:
            text = f.read()
    else:
        text = bpath
    generator = Generator(text)
else:
    generator = Generator()
args = parse_args()
print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))