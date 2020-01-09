from gitter_chat_recognition.link_checker import link_checker
from googlesearch import search


def google_search(query_test):
    query = 'gitter ' + query_test
    my_results_list = []
    for i in search(query,  # The query you want to run
                    tld='com',  # The top level domain
                    lang='en',  # The language
                    num=10,  # Number of results per page
                    start=0,  # First result to retrieve
                    stop=3,  # Last result to retrieve
                    pause=2.0,  # Lapse between HTTP requests
                    ):
        my_results_list.append(i)
    for elem in my_results_list:
        if link_checker(elem, query_test) is not None:
            return elem
    return None
