import requests
from operator import itemgetter

# 这个API调用返回一个列表， 其中包含Hacker News上当前最热门的500篇文章的ID。 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json() # ID列表
submission_dicts = []
for submission_id in submission_ids[:30]: # 取前30名的ID
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # 摘取需要的内容
    submission_dict = {
        'title' : response_dict['title'],
        'link' : 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments' : response_dict.get('descendants', 0) # 不确定某个键是否包含在字典中时， 可使用方法dict.get() ， 
                                                         # 它在指定的键存在时返回与之相关联的值， 并在指定的键不存在时返回你指定的值（这里是0） 
    }
    submission_dicts.append(submission_dict)

# 对得到的字典列表按照'comments'所对应的键值降序排列
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])  