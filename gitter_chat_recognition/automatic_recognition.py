import requests


def get_project_name(org):
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
        try:
            for elem in rep.json():
                repo_list_full_name.append(elem['full_name'])
                repo_list.append(elem['name'])
            if(len(rep.json()) == 0):
                break
        except TypeError:
            return ('Project not found')
    return repo_list_full_name


def gitter_chat_full_project_name(project_name):
    url = 'https://gitter.im/' + project_name
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    else:
        return url


def gitter_chat_project_name(project_name):
    url = 'https://gitter.im/' + project_name + "/" + project_name
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    else:
        return url


def gitter_badge(project_name):
    url = 'https://github.com/' + project_name
    finder = 'https://gitter.im'
    requester = requests.get(url)
    text = requester.text.split()
    for elem in text:
        if str(elem).find(finder) != -1:
            list = elem.split('href="')
            if list[1].find('?utm_source') != -1:
                link_gitter = list[1].split('?utm_source')[0]
                return link_gitter
            else:
                link_gitter = list[1].split('"')[0]
                return link_gitter
    return None


def reading_contributing(project_name):
    url = 'https://github.com/' + project_name + '/blob/master/CONTRIBUTING.md'
    finder = 'https://gitter.im'
    requester = requests.get(url)
    text = requester.text.split()
    for elem in text:
        if str(elem).find(finder) != -1:
            list = elem.split('href="')
            if list[1].find('?utm_source'):
                link_gitter = list[1].split('?utm_source')[0]
            else:
                link_gitter = list[1].split('"')[0]
            return link_gitter
    return None


'''gitter_badge('flutter/flutter')
get_room_link('rails')
get_room_link('laravel')
get_room_link('elixir-lang')
get_room_link('JabRef')
get_room_link('github')
get_room_link('atom')
get_room_link('flutter')
get_room_link('ionic-team')
test_gitter_chat('JabRef/jabref')
test_gitter_chat('atom/atom')'''
