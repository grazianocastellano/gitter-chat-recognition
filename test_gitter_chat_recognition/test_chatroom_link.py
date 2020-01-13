import unittest

from gitter_chat_recognition.chatroom_link import link_retrevier


class Test_Chatroom_link(unittest.TestCase):

    def test_chatroom_link(self):
        self.assertEqual(link_retrevier('flutter/flutter', 'flutter'),
                         'flutter/flutter')

    def test_chatroom_link1(self):
        self.assertIsNone(link_retrevier('atom/atom', 'atom'))

    def test_chatroom_link2(self):
        self.assertEqual(link_retrevier('microsoft/TypeScript', 'TypeScript'),
                         'https://gitter.im/microsoft/TypeScript')


if __name__ == "__main__":
    unittest.main()
