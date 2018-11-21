from . import parse
import sys
import argparse

def parse_args(args):
    """
    Parses arguments
    """
    parser = argparse.ArgumentParser(prog='ijkl')
    parser.add_argument('template', help='Template file to process')
    parser.add_argument('-o', '--output', default='config.out',
            help='Output file')
    parser.add_argument('-P', '--parent', default='~/.config/i3',
            type=str, help='Parent directory to look files in')
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    try:
        template = open(args.template, 'r')
    except OSError:
        raise OSError("Error: Cannot open {}".format(args.template))

    try:
        output = open(args.output, 'w')
    except OSError:
        template.close()
        raise OSError("Error: Cannot open {}".format(args.output))

    config = parse(template.read())

    output.write(config)

    output.close()
    template.close()
