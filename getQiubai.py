import sys
sys.path.append('util/')
import requests
from getConfig import *
result = {}

def getJson(count,head,url,parameter):
    items = []
    item = {}
    result['count'] = count;
    data = requests.get(url,headers=head,params=parameter)
    data = data.json()
    for old_item in data['items']:
        item = {}
        item['content'] = old_item['content']
        item['votes'] = old_item['votes']
        # item['type'] = old_item['format']
        if old_item['format'] != 'word':
            print (old_item['format'])
            item['type'] = old_item['format']
            item['url'] = old_item['high_loc']
        else:
            item['type'] = old_item['format']
        try:
            item['user'] = {'name':str(old_item['user']['login']),'image':str(old_item['user']['medium'])}
        except:
            item['user'] = 'null'
        if old_item.__contains__('hot_comment'):
            item['hashot'] = str('True')
            item['hot_comment'] = {'content':str(old_item['hot_comment']['content']),'user':{'name':(old_item['hot_comment']['user']['login'])}}
        else:
            item['hashot'] = str('False')
        items.append(item)
        if (len(items) == int(count)):
            break
    result['items'] = items
    return result
def run(page = '1',typere = 'fresh',count = 30):
    global result
    head={};result={}
    head['User-Agent'] = getHead()
    para = {
    'page':page,
    'typere':typere,
    'count':count
    }
    return getJson(count,head,getQiubai(),para)
if __name__ == '__main__':
    run()