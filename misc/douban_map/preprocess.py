# coding: UTF-8
# 国内豆瓣用户地理分布数据统计
# -- mckelvin
import requests
from filecache import filecache
import json

def get_name_dict():
    names = {
		'heilongjiang': '黑龙江',
		'jilin': '吉林', 
		'liaoning': '辽宁', 
		'hebei': '河北', 
		'shandong': '山东', 
		'jiangsu': '江苏', 
		'zhejiang': '浙江', 
		'anhui': '安徽', 
		'henan': '河南', 
		'shanxi': '山西', 
		'shaanxi': '陕西', 
		'gansu': '甘肃', 
		'hubei': '湖北', 
		'jiangxi': '江西', 
		'fujian': '福建', 
		'hunan': '湖南', 
		'guizhou': '贵州', 
		'sichuan': '四川', 
		'yunnan': '云南', 
		'qinghai': '青海', 
		'hainan': '海南', 
		'shanghai': '上海', 
		'chongqing': '重庆', 
		'tianjin': '天津', 
		'beijing': '北京', 
		'ningxia': '宁夏', 
		'neimongol': '内蒙古', 
		'guangxi': '广西', 
		'xinjiang': '新疆', 
		'xizang': '西藏', 
		'guangdong': '广东', 
		'hongkong': '香港', 
		'taiwan': '臺灣', 
		'macau': '澳门'
	}
    return dict((v,k) for k,v in names.iteritems())

@filecache
def retrieval_data():
    url_mainland = 'http://www.douban.com/j/location/china/' # mainland
    url_world = 'http://www.douban.com/j/location/zone/' # world
    res_world = requests.get(url_world)
    res_mainland = requests.get(url_mainland)
    return res_world.text.encode('utf-8'), res_mainland.text.encode('utf-8')

def get_population_data():
    res_world, res_mainland = retrieval_data()
    json_world = json.loads(res_world)
    json_mainland = json.loads(res_mainland)
    json_china = json_mainland
    json_other_parts = filter(lambda loc: loc.get('name') in [u'香港', u'臺灣', u'澳门'],json_world.get('locations'))
    json_china.update({'locations': json_china.get('locations')+json_other_parts})
    return json_china

def main():
    population_data = get_population_data()
    name_dict = get_name_dict()
    assert population_data.get('r') == True
    with open('douban_population.tmpl') as fh:
        template = ''.join(fh.readlines())
    
    prov_pop_list = []
    pop_list = []
    for loc in population_data.get('locations'):
        province_id = name_dict.get(loc.get('name').encode('utf-8'))
        population = loc.get('population')
        assert province_id is not None
        prov_pop_list.append((province_id, population))
        pop_list.append(population)
    
    render_str= '{' # 必须输出有序字典
    for i, (province_id, population) in enumerate(sorted(prov_pop_list, key=lambda a: a[1],reverse=True)):
        state_color = 6 - int(round(6. * (population - min(pop_list)) / (max(pop_list) - min(pop_list)))) # [0,6] in 7 bars
        print i, province_id, population, state_color
        render_str += ''''%s': {'stateInitColor': %s, 'value': %s},''' % (province_id, state_color, population)
    render_str += '}'
    with open('douban_population.html', 'w') as fh:
        fh.write(template.replace('{data}', render_str))

if __name__ == '__main__':
    main()
