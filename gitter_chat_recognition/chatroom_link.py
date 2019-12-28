from gitterpy.client import GitterClient

import google_search
from automatic_recognition import (gitter_chat_full_project_name,
                                   gitter_chat_project_name)


def get_chat_link(full_project_name, name_project, token):
    client = GitterClient(token)
    if gitter_chat_full_project_name(full_project_name) is None:
        client.rooms.join(full_project_name)
        client.messages.get_all_messages(full_project_name)
    elif gitter_chat_project_name is None:
        room_name = name_project + "/" + name_project
        client.rooms.join(room_name)
        client.messages.get_all_messages(room_name)
    else:
        roomchat = google_search.google_search(name_project)
        client.rooms.join(roomchat)
        client.messages.get_all_messages(roomchat)
