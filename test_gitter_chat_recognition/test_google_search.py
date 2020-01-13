import unittest

from gitter_chat_recognition.google_search import google_search


class Test_Google_Search(unittest.TestCase):

    def test_google_search(self):
        self.assertEqual(google_search('flutter/flutter'),
                         'https://gitter.im/flutter/flutter')

    def test_google_search2(self):
        self.assertIsNone(google_search('facebook/react'))


if __name__ == "__main__":
    unittest.main()
