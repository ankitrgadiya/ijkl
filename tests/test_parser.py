import sys
sys.path.append('../ijkl')

from ijkl.parser import include, parse, WrongSyntax
import unittest


class parser_parse(unittest.TestCase):
    """
    Tests parse function from parser module
    """

    def test_comment(self):
        self.assertEqual(parse('# This is a comment'), '')

    def test_empty_line(self):
        self.assertEqual(parse('\n'), '')

    def test_tab(self):
        self.assertEqual(parse('\t'), '')

    def test_valid_config(self):
        self.assertEqual(parse('set $mod Mod4'), 'set $mod Mod4')

    def test_include_without_file(self):
        with self.assertRaises(WrongSyntax):
            parse('include ')

    def test_include_with_multiple_file(self):
        with self.assertRaises(WrongSyntax):
            parse('include test1 test2')


class parser_include(unittest.TestCase):
    """
    Tests include function from parser module
    """

    def test_no_file(self):
        with self.assertRaises(OSError):
            include('no_file')

    def test_empty_file(self):
        self.assertEqual(include('empty', folder='tests/files'), '')

    def test_valid_file(self):
        self.assertEqual(include('valid', folder='tests/files'),
                'set $mod Mod4\n')

    def test_valid_file_with_path(self):
        self.assertEqual(include('tests/files/valid'), 'set $mod Mod4\n')

    @unittest.expectedFailure
    def test_valid_file_with_include(self):
        self.assertEqual(include('valid_with_include', folder='tests/files'),
                'set $mod Mod4\n')


if __name__ == "__main__":
    unittest.main()
