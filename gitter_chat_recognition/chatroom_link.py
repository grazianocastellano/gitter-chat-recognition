from gitter_chat_recognition.automatic_recognition import \
    gitter_badge as gitter_badge
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_full_project_name as gitter_chat_full_project_name
from gitter_chat_recognition.automatic_recognition import \
    gitter_chat_project_name as gitter_chat_project_name
from gitter_chat_recognition.google_search import google_search


def link_retrevier(full_project_name, name_project):
    link_return = gitter_badge(full_project_name)
    if link_return is not None:
        return link_return
    elif gitter_chat_full_project_name(full_project_name) is not None:
        return gitter_chat_full_project_name(full_project_name)
    elif gitter_chat_project_name(name_project) is not None:
        return gitter_chat_project_name(name_project)
    elif google_search(full_project_name) is not None:
        return google_search(full_project_name)
    else:
        return None
