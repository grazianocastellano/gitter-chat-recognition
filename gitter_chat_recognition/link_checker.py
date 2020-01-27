import re

import requests


def link_checker(url, project_name):
    html = requests.get(url).text.split()
    finder = 'github.com/' + project_name
    for elem in html:
        if elem.find(finder) != -1:
            list = elem.split('href="')
            if(list[1].find('issues') != -1):
                link_github = list[1].split('/issues/')[0]
            else:
                link_github = list[1].split('"')[0]
            if(requests.get(link_github).status_code == 200):
                return link_github
    return None


def link_checker_beta(url, project_name):
    gitter_id = url.split('gitter.im/')[1]
    github_url = 'https://github.com/' + gitter_id
    github_project = 'https://github.com/'+project_name
    resp = requests.get(github_url)
    if resp.status_code != 200:
        # TODO
        # Aggiungere controllo tra nome della lobby e nome del progetto
        split_gitter_name = re.split(r'\W+', gitter_id)
        split_project_name = re.split(r'\W+', project_name.split('/')[1])
        temp = False
        for elem in split_project_name:
            for elem2 in split_gitter_name:
                if elem2.find(elem) != -1:
                    resp2 = requests.get(github_project)
                    if resp2.status_code == 200:
                        temp = True
        if(temp is True):
            return github_project
        else:
            return None
    else:
        html = resp.text.split()
        for elem in html:
            if elem.find(github_project) != -1:
                return github_project
