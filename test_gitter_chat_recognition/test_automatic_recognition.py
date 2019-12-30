import unittest

from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_full_project_name as gitter_chat_full_project_name
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_project_name


class Test_Automatic_Recognition(unittest.TestCase):

    def test_gitter_chat_full_project_name(self):
        self.assertEqual(gitter_chat_full_project_name('JabRef/jabref'),
                         'https://gitter.im/JabRef/jabref')

    def test_gitter_chat_project_name(self):
        self.assertEqual(gitter_chat_project_name('vscode'),
                         None)


if __name__ == '__main__':
    unittest.main()
