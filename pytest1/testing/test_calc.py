#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
from pytest1.pytestCode.calculator import Calculator

#读取测试数据 111
def get_datas():
    with open('./datas/calc.yml',encoding='utf-8') as f:
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

        divdatas = mydatas['div']['datas']
        divmyids = mydatas['div']['myids']
        div_wrongdatas = mydatas['div_wrong']['datas']
        div_wrongids = mydatas['div_wrong']['myids']

    return [adddatas,addmyids,add_wrongdatas,add_wrongids,
            subdatas,submyids,sub_wrongdatas,sub_wrongids,
            divdatas,divmyids,div_wrongdatas,div_wrongids

            ]
class TestCalculator:
    #类级别
    def setup_class(self):
        print('setup_class:开始计算')
        self.calc = Calculator()


    def teardown_class(self):
        print("teardown:结束计算")

    # #方法级别
    # def setup(self):
    #     print('开始计算')
    #
    # def teardown(self):
    #     print("结束计算")

    #加法测试用例
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',get_datas()[0] ,ids=get_datas()[1])
    def test_add(self,a,b,expect):
        print('加法正确的测试用例')
        result = self.calc.add(a,b)
        assert result==expect

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_add_wrong(self,a,b,expect):
        print('加法错误的测试用例')
        result = self.calc.add(a,b)
        assert result==expect

    #减法测试用例
    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_sub(self,a,b,expect):
        print('减法正确的测试用例')
        result = round(self.calc.sub(a,b),2)
        assert result==expect

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,expect', get_datas()[6], ids=get_datas()[7])
    def test_sub_wrong(self,a,b,expect):
        print('减法错误的测试用例')
        result = self.calc.sub(a,b)
        assert result==expect
    #
    # # #乘法测试用例
    # @pytest.mark.mul
    # def test_mul(self,a,b,expect):
    #     print('乘法正确的测试用例')
    #     result = self.calc.mul(a,b)
    #     assert result==expect
    #
    # @pytest.mark.mul
    # def test_mul_wrong(self,a,b,expect):
    #     print('乘法错误的测试用例')
    #     result = self.calc.mul(a,b,)
    #     assert result==expect

    #除法测试用例
    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', get_datas()[8], ids=get_datas()[9])
    def test_div(self,a,b,expect):
        print('除法正确的测试用例')
        result = self.calc.div(a,b)
        assert result==expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[10], ids=get_datas()[11])
    def test_div_wrong(self,a,b,expect):
        print('除法错误的测试用例')
        result = self.calc.div(a,b)
        assert result==expect