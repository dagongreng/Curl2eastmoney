import json
import requests

cookies = {
    'cowCookie': 'true',
    'qgqp_b_id': '8d8043203fba760bb8b542e82186c78e',
    'st_si': '07211380195389',
    'waptgshowtime': '20201128',
    'intellpositionL': '536px',
    'cowminicookie': 'true',
    'st_asi': 'delete',
    'intellpositionT': '855px',
    'st_pvi': '91963319216679',
    'st_sp': '2020-11-28^%^2016^%^3A12^%^3A55',
    'st_inirUrl': 'http^%^3A^%^2F^%^2Fdata.eastmoney.com^%^2F',
    'st_sn': '30',
    'st_psi': '20201128200354596-113300300814-8314618200',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid', 'f184^'),
    ('fid0', 'f4001^'),
    ('fields', 'f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('rt', '53552167^'),
    # ('cb', 'jQuery18304228299329987295_1606565013248^'),
    ('_', '1606565038074'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)

#print(response)
#print(response.text)

# print(type(response.text))

resp_dict = json.loads(response.text)
# print(type(resp_dict))
# print(resp_dict)

datas = resp_dict.get('data').get('diff')
# print(datas)
companies = []
prices = []


for data in datas:
    print(data)
    company = data.get('f14')
    share_1 = data.get('f184')
    share_5 = data.get('f165')
    share_10 = data.get('f175')

    # print(type(share_5))
    price = data.get('f2')

    if share_1 >= 5 and share_5 >= 10 and share_10 >= 5:
        companies.append(company)
        prices.append(price)

# print(companies)
# print(prices)

from pyecharts.charts import Bar
import pyecharts.options as opts

bar = Bar()
bar.add_xaxis(companies)
bar.add_yaxis('股价图',prices)

bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=-40),
    ),
    yaxis_opts=opts.AxisOpts(name='价格：（元/股）'),
    )


bar.render('股价图.html')

#字典
# dict = {'a':1,'b':2,'c':{'d':3}}

#print(dirt['a'])
#print(dict.get('c').get('d'))

#列表
# list=[1,2,3,4,5]
# list.append(6)
# for i in list:
#     print(i)