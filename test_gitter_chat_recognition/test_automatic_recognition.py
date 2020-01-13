import unittest

from gitter_chat_recognition.automatic_recognition import \
    get_project_name as get_project_name
from gitter_chat_recognition.automatic_recognition import \
    gitter_badge as gitter_badge
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_full_project_name as gitter_chat_full_project_name
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_project_name as gitter_chat_project_name


class Test_Automatic_Recognition(unittest.TestCase):

    def test_gitter_chat_full_project_name(self):
        self.assertEqual(gitter_chat_full_project_name('JabRef/jabref'),
                         'https://gitter.im/JabRef/jabref')

    def test_gitter_chat_project_name(self):
        self.assertEqual(gitter_chat_project_name('vscode'),
                         None)

    def test_get_project_name(self):
        list1 = ['gitter-chat-recognition', 'GitterPy', 'grimoirelab-perceval']
        self.assertEqual(get_project_name('grazianocastellano'), list1)

    def test_gitter_badge(self):
        self.assertEqual(gitter_badge('flutter/flutter'), 'flutter/flutter')

    def test_gitter_badge2(self):
        self.assertEqual(gitter_badge('grazianocastellano/Gitterpy'), None)


if __name__ == '__main__':
    unittest.main()
