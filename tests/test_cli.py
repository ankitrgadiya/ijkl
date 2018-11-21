import sys
sys.path.append('../ijkl')

from ijkl.cli import parse_args
import unittest

class cli_parse_args(unittest.TestCase):
    """
    Tests parse_args function from cli module
    """

    def test_output_default(self):
        args = parse_args(['config.templ'])
        self.assertEqual(args.output, 'config.out')

    def test_output_short(self):
        args = parse_args(['-o', 'config', 'config.templ'])
        self.assertEqual(args.output, 'config')

    def test_output_long(self):
        args = parse_args(['--output', 'config', 'config.templ'])
        self.assertEqual(args.output, 'config')

    def test_parent_default(self):
        args = parse_args(['config.templ'])
        self.assertEqual(args.parent, '~/.config/i3')

    def test_parent_short(self):
        args = parse_args(['-P', '~/.i3', 'config.templ'])
        self.assertEqual(args.parent, '~/.i3')

    def test_parent_long(self):
        args = parse_args(['--parent', '~/.i3', 'config.templ'])
        self.assertEqual(args.parent, '~/.i3')


if __name__ == "__main__":
    unittest.main()
