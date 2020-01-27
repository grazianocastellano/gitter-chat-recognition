import time

from gitter_chat_recognition.link_checker import link_checker as link_checker
from googleapiclient.discovery import build


def google_search_auth(query_test):
    api_key = "AIzaSyARUpnmrJhz2BNh45rDhpnK5vlCrortnUM"
    cse_id = "016258605236218919930:fvbht5wuhx6"
    service = build("customsearch", "v1", developerKey=api_key).cse()
    res = service.list(q=query_test, cx=cse_id, num=3).execute()
    list_link = []
    try:
        list_res = res['items']
        for elem in list_res:
            if(elem['link'].find('https://gitter.im') != -1 and
               elem['link'].find('https://gitter.im/explore') == -1):
                list_link.append(elem['link'])
    except:
        return list_link
    return list_link


def google_search(query_test):
    time.sleep(2.0)
    query = 'gitter ' + query_test
    my_results_list = []
    res = google_search_auth(query)
    for i in res:
        if(i.find('https://gitter.im') != -1):
            my_results_list.append(i)
    for elem in my_results_list:
        link = elem.split('?')[0]
        if link_checker(link, query_test) is not None:
            return link
    return None
