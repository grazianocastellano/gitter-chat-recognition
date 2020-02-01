from gitter_chat_recognition.automatic_recognition import get_project_name
from gitter_chat_recognition.chatroom_link import link_retrevier
from sys import exit


def list_of_repos(org_name):
    repos = []
    namefile_repos = org_name + '_repos.txt'
    namematrix_file = org_name + '_matrix.txt'
    try:
        file = open(namefile_repos, 'r')
        get_list = file.read()
        repos = get_list.split()
        file.close()
        matrix_generator(namematrix_file, repos)
    except FileNotFoundError:
        file = open(namefile_repos, 'w')
        repos = get_project_name(org_name)
        for repo in repos:
            file.write((repo + ' '))
        file.close()
        matrix_generator(namematrix_file, repos)
    

def matrix_generator(namematrix_file, repos):
    matrix = []
    try:
        matrix = get_matrix_from_file(namematrix_file)
        print(matrix)
        for repo_elem in repos:
            found = False
            for couple in matrix:
                if couple[0] == repo_elem:
                    found = True
            if found is False:
                try:
                    link_chatroom = link_retrevier(repo_elem)
                    matrix.append([repo_elem, link_chatroom])
                except httpError:
                    print('Termino a causa del limite di ricerche giornaliere')
        write_matrix_in_file(matrix, namematrix_file)
    except FileNotFoundError:
        for repo in repos:
            try:
                link_chatroom = link_retrevier(repo)
                if link_chatroom is not None:
                    matrix.append([repo, link_chatroom])
                else:
                    matrix.append([repo, None])
            except httpError:
                print('Termino a causa del limite di ricerche giornaliere')
                break
        write_matrix_in_file(matrix, namematrix_file)
    print(len(matrix))


def get_matrix_from_file(nameFile):
    file_matrix = open(nameFile, 'r')
    linear_matrix = file_matrix.read().split()
    matrix = []
    i = 0
    while i< len(linear_matrix):
        matrix.append([linear_matrix[i], linear_matrix[i+1]])
        i=i+2
    file_matrix.close()
    return matrix
    # gestire httpError


def write_matrix_in_file(matrix, name_file):
    file_matrix = open(name_file, 'w')
    for elem in matrix:
        file_matrix.write((str(elem[0]) + ' '))
        file_matrix.write((str(elem[1]) + ' '))
    file_matrix.close()
    

list_of_repos('elixir-lang')
