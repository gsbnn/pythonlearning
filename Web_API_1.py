import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# API命令格式
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# 执行API调用
r = requests.get(url) # 返回一个Responce对象（实例）
print("Status code:", r.status_code) # r.status_code = 200 表示响应成功

# Returns the json-encoded content of a response
# 已知返回格式为：dict{'total_count': value, 'incomplete_results': value, 'items': list[dict{}, dict{},...]}
response_dict = r.json()
print(response_dict.keys()) # 返回一个字典
print("Total repositories:", response_dict['total_count'])

# 研究仓库信息
repo_dicts = response_dict['items'] # 返回一个列表
print("Repositories returned:", len(repo_dicts)) # 列表中共有30项，即共30个仓库

"""
# 研究第一个仓库
repo_dict = repo_dicts[0] # 返回一个字典（列表的第一项），即第一个仓库
print("\nKeys:", len(repo_dict)) # 返回描述仓库的条目数
for key in sorted(repo_dict.keys()):
    print(key)
print("\nSelected information about first repository")
print('Name:', repo_dict['name']) # 项目名
print('Owner:', repo_dict['owner']['login']) # 登录名
print('Stars:', repo_dict['stargazers_count']) # 获得星数
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at']) # 项目创建时间
print('Updated:', repo_dict['updated_at']) # 最后一次更新时间
print('Description:', repo_dict['description'])
"""

# 添加自定义工具提示
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value' : repo_dict['stargazers_count'], 
        'label' : repo_dict['description'],
        'xlink' : repo_dict['html_url'], # 在图表中添加可单击的链接
    }
    plot_dicts.append(plot_dict) # 添加自定义工具提示,plot_dicts是一个list[dict,dict,...]

my_style = LS(color='#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15 # 缩减名称
my_config.show_y_guides = True # 显示水平线
my_config.width = 1000 # 设置图表宽度
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github' # 图片标题
chart.x_labels = names # 设置横坐标标签
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')