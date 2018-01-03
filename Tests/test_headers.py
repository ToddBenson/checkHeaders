import unittest
import headers
import os


class TestHeaders(unittest.TestCase):
    """Test headers.py"""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.targets_filename = 'targets.txt'
        with open(self.targets_filename, 'w') as f:
            f.write('https://www.facebook.com\n'
                    'https://www.twitter.com\n'
                    'https://www.linkedin.com\n'
                    'yahoo.com\n'
                    'https://www.google.com')

        self.default_headers_filename = "default-headers.txt"
        with open(self.default_headers_filename, 'w') as f:
            f.write('X-Frame-Options\n'
                    'Content-Security-Policy\n'
                    'X-Content-Type-Options\n'
                    'Cache-Control\n'
                    'X-XSS-Protection\n'
                    'Server\n'
                    'Referrer-Policy\n'
                    'Public-Key-Pins\n'
                    'Strict-Transport-Policy')

        self.headers_filename = 'headers.txt'
        with open(self.headers_filename, 'w') as f:
            f.write('Server')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.targets_filename)
            os.remove(self.headers_filename)
        except:
            raise

    def test_function_runs(self):
        headers.get_headers_to_check(None)

    def test_get_targets(self):
        self.assertEqual(headers.get_targets(self.targets_filename)[2], "https://www.linkedin.com")

    def test_check_headers_fail(self):
        self.assertEqual(headers.check_headers('dshjgfads', None), "['dshjgfads', 'Invalid URL']")

    def test_check_headers(self):
        self.assertEqual(headers.check_headers('https://www.linkedin.com', None)[0], 'https://www.linkedin.com')

    def test_get_headers_file(self):
        self.assertEqual(headers.get_headers_to_check(self.headers_filename), ['Server'])

    def test_get_headers_default(self):
        self.assertEqual(headers.get_headers_to_check(None), ['X-Frame-Options',
                                                              'Content-Security-Policy',
                                                              'X-Content-Type-Options',
                                                              'Cache-Control',
                                                              'X-XSS-Protection',
                                                              'Server',
                                                              'Referrer-Policy',
                                                              'Public-Key-Pins',
                                                              'Strict-Transport-Policy'])

    def test_check_targets(self):
        self.assertEqual(headers.check_targets(self.targets_filename, self.headers_filename)[0][2],
                         'Server: header not found')

    def test_main_runs(self):
        with self.assertRaises(SystemExit):
            headers.main()

    def test_parser_url(self):
        parser = headers.parse_args(['-u https://www.linkedin.com'])
        self.assertTrue(parser.url)

    def test_parser_print(self):
        parser = headers.parse_args(['-p'])
        self.assertTrue(parser.printheader)

    def test_parser_file(self):
        parser = headers.parse_args(['-f ./targets.txt'])
        self.assertTrue(parser.file)

    def test_parser_response(self):
        parser = headers.parse_args(['-r ./headers.txt'])
        self.assertTrue(parser.response)

    # refactor following two tests to be stand alone
    def test_check_arguments_none(self):
        with self.assertRaises(SystemExit):
            headers.check_arguments(headers.parse_args(['-p']))

    def test_check_arguments_both(self):
        with self.assertRaises(SystemExit):
            headers.check_arguments(headers.parse_args(['-u https://www.linkedin.com', '-f ./targets.txt']))

