import requests


def get_room_link(org):
    page_number = 0
    number_repository = 0
    repo_list_full_name = []
    repo_list = []
    while True:
        page_number += 1
        url = 'https://api.github.com/users/'
        url += org + '/repos?page='
        url += str(page_number) + '&per_page=100'
        rep = requests.get(url)
        number_repository += len(rep.json())
        for elem in rep.json():
            repo_list_full_name.append(elem['full_name'])
            repo_list.append(elem['name'])
        if(len(rep.json()) == 0):
            break


def gitter_chat_full_project_name(project_name):
    url = 'https://gitter.im/' + project_name
    resp = requests.get(url)
    if resp.status_code != 200:
        return url
    else:
        return None


def gitter_chat_project_name(project_name):
    url = 'https://gitter.im/' + project_name + "/" + project_name
    resp = requests.get(url)
    if resp.status_code != 200:
        return url
    else:
        return None



'''get_room_link('rails')
get_room_link('laravel')
get_room_link('elixir-lang')
get_room_link('JabRef')
get_room_link('github')
get_room_link('atom')
get_room_link('flutter')
get_room_link('ionic-team')
test_gitter_chat('JabRef/jabref')
test_gitter_chat('atom/atom')'''
