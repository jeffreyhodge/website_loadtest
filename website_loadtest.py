import requests
from concurrent.futures import ThreadPoolExecutor

max_workers = 100

url = ["http://yahoo.com/"]

list_of_urls = url * max_workers

#def get_url(url):
#    return requests.get(url)

def get_url(url):
    try:
        r = str(requests.get(url))
    except requests.exceptions.RequestException as e:
        r = e
    return r

with ThreadPoolExecutor(max_workers) as pool:
    resp_list = list(pool.map(get_url,list_of_urls))

results_dict = {}
for resp in resp_list:
    results_dict[resp] = resp_list.count(resp)

for k,v in results_dict.iteritems():
    print("%d : %s" % (v,k))
