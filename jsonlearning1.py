import json
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from world_population import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # pop_data是一个列表，每个元素是一个字典

# 获取国别码和人口数量
cc_populations = {} # 空字典
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010': # 寻找2010年各个国家的人口数量
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name) # 获取国别码
        if code:
            cc_populations[code] = population # 将国别码和人口数量装入字典
            print(code + ":" + str(population))
        else:
            print('ERROR - ' + country_name)

# 人口分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 创建地图
wm_style = RS(color='#9966FF', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm._title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')