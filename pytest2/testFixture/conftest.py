#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import List

import pytest
import yaml

from pytest2.pytest_fixture.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope="class")
def get_calc():
    print('开始计算')
    calc = Calculator()
    yield calc
    print("结束计算")


def get_datas():
    #获取测试数据的绝对路径
    mydataspath = os.path.dirname(__file__) +"/datas/calc.yml"
    with open(mydataspath,encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        #加法
        adddatas = mydatas['add']['datas']
        addmyids = mydatas['add']['myids']
        add_wrongdatas = mydatas['add_wrong']['datas']
        add_wrongids = mydatas['add_wrong']['myids']

        subdatas = mydatas['sub']['datas']
        submyids = mydatas['sub']['myids']
        sub_wrongdatas = mydatas['sub_wrong']['datas']
        sub_wrongids = mydatas['sub_wrong']['myids']

        muldatas = mydatas['mul']['datas']
        mulmyids = mydatas['mul']['myids']
        mul_wrongdatas = mydatas['mul_wrong']['datas']
        mul_wrongids = mydatas['mul_wrong']['myids']

        divdatas = mydatas['div']['datas']
        divmyids = mydatas['div']['myids']
        div_wrongdatas = mydatas['div_wrong']['datas']
        div_wrongids = mydatas['div_wrong']['myids']

    return [adddatas,addmyids,add_wrongdatas,add_wrongids,
            subdatas,submyids,sub_wrongdatas,sub_wrongids,
            muldatas,mulmyids,mul_wrongdatas,mul_wrongids,
            divdatas,divmyids,div_wrongdatas,div_wrongids

            ]
@pytest.fixture(params=get_datas()[0] ,ids=get_datas()[1])
def get_datas1(request):
    return request.param

@pytest.fixture(params=get_datas()[2] ,ids=get_datas()[3])
def get_datas2(request):
    return request.param

@pytest.fixture(params=get_datas()[4] ,ids=get_datas()[5])
def get_datas3(request):
    return request.param

@pytest.fixture(params=get_datas()[6] ,ids=get_datas()[7])
def get_datas4(request):
    return request.param

@pytest.fixture(params=get_datas()[8] ,ids=get_datas()[9])
def get_datas5(request):
    return request.param

@pytest.fixture(params=get_datas()[10] ,ids=get_datas()[11])
def get_datas6(request):
    return request.param

@pytest.fixture(params=get_datas()[12] ,ids=get_datas()[13])
def get_datas7(request):
    return request.param

@pytest.fixture(params=get_datas()[14] ,ids=get_datas()[15])
def get_datas8(request):
    return request.param
