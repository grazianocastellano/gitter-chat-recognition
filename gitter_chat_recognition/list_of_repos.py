from gitter_chat_recognition.automatic_recognition import get_project_name
from gitter_chat_recognition.chatroom_link import link_retrevier


def list_of_repos(org_name):
    list = get_project_name(org_name)
    matrix = []
    try:
        for elem in list:
            print(elem)
            gitter_link = link_retrevier(elem, elem.split('/')[1])
            if(gitter_link) is not None:
                print(gitter_link)
                matrix.append([elem, gitter_link])
            else:
                matrix.append([elem, None])
        print(matrix)
        with open(org_name + '.txt', "w") as openfile:
            openfile.write(matrix)
        openfile.close()
    except:
        print('Users not Found')


list_of_repos('flutter')