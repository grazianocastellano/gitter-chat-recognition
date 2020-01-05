import requests


def link_checker(url, project_name):
    html = requests.get(url).text.split()
    finder = 'github.com/' + project_name 
    for elem in html:
        if elem.find(finder)!= -1:
            list = elem.split('href="')
            link_github = list[1].split('"')[0]
            return(link_github)
    return None
            


print(link_checker('https://gitter.im/flutter/flutter','flutter/flutter'))