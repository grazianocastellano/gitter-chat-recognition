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
            if(requests.get(link_github).status_code != 200):
                return None
            else:
                return link_github
    return None
