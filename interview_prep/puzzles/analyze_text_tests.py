import unittest
import os
from interview_prep.puzzles.analyze_text import analyze_text


class AnalyzeTextTests(unittest.TestCase):
    """Tests for the ''analyze_text()'' function."""

    def setUp(self):
        """Fixture to create a file to test"""
        self.filename = 'analyze_text_file.txt'
        with open(self.filename, 'w') as f:
            f.write('We the People of the United States, in Order to form a more perfect Union, establish Justice, '
                    'insure domestic Tranquility, provide for the common defence, promote the general Welfare, '
                    'and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish '
                    'this Constitution for the United States of America.\n'
                    'Article. I.\nArticle. I.\n'
                    'All legislative Powers herein granted shall be vested in a Congress of the United States, '
                    'which shall consist of a Senate and House of Representatives.\n'
                    'Section. 2.\nThe House of Representatives shall be composed of Members chosen every second '
                    'Year by the People of the several States, and the Electors in each State shall have the '
                    'Qualifications requisite for Electors of the most numerous Branch of the State Legislature.')

    def tearDown(self):
        """Fixture to delete test file"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_numbers(self):
        self.assertEqual(6, analyze_text(self.filename)[0])

    def test_char_numbers(self):
        self.assertEqual(773, analyze_text(self.filename)[1])

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foo')

    def test_no_deletion(self):
        """Check that function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()