import unittest

from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_full_project_name as gitter_chat_full_project_name
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_project_name as gitter_chat_project_name
from gitter_chat_recognition.automatic_recognition import get_project_name


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


if __name__ == '__main__':
    unittest.main()
