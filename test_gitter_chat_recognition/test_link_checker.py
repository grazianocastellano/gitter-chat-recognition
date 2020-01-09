import unittest

from gitter_chat_recognition.link_checker import link_checker


class Test_Link_Checker(unittest.TestCase):

    def test_link_checker(self):
        self.assertEqual(link_checker('https://gitter.im/flutter/flutter',
                                      'flutter/flutter'),
                         'https://github.com/flutter/flutter')

    def test_link_checker2(self):
        self.assertEqual(link_checker('https://gitter.im/duojs/duo',
                                      'duojs/duo'),
                         'https://github.com/duojs/duo')

    def test_link_checker3(self):
        self.assertEqual(link_checker('https://gitter.im/Microsoft/vscode',
                                      'microsoft/vscode'),
                         'https://github.com/microsoft/vscode')

    def test_link_checker4(self):
        self.assertEqual(link_checker('https://gitter.im/ant-design/ant-design-english',
                                      'ant-design/ant-design'),
                         'https://github.com/ant-design/ant-design')

    def test_link_checker5(self):
        self.assertIsNone(link_checker('https://gitter.im/communityTest/commytest',
                                       'communityTest/commytest'))


if __name__ == '__main__':
    unittest.main()
