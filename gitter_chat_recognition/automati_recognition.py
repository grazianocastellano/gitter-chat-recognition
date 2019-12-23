import requests
import json

def get_room_link(org):
    page_number = 0
    number_repository = 0
    repo_list = []
    while True:
        page_number +=1
        url = 'https://api.github.com/users/' + org + '/repos?page=' + str(page_number) + '&per_page=100'
        rep = requests.get(url)
        number_repository += len(rep.json())
        for elem in rep.json():
            repo_list.append(elem['full_name'])
        if(len(rep.json())==0):
            break
    print(number_repository)
    print(repo_list)
    

#get_room_link('rails')
'''get_room_link('laravel')
get_room_link('elixir-lang')
get_room_link('JabRef')
get_room_link('github')
get_room_link('atom')
get_room_link('flutter')'''
get_room_link('ionic-team')