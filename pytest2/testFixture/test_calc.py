#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml


#读取测试数据
from pytest2.pytest_fixture.calculator import Calculator

class TestCalculator:
    #类级别
    # def setup_class(self):
    #     print('setup_class:开始计算')
    #     self.calc = Calculator()
    #
    #
    #
    # def teardown_class(self):
    #     print("teardown:结束计算")

    # #方法级别
    # def setup(self):
    #     print('开始计算')
    #
    # def teardown(self):
    #     print("结束计算")

    #加法测试用例
    @pytest.mark.add
    @pytest.mark.run(order=1)
   # @pytest.mark.parametrize('a,b,expect',get_datas()[0] ,ids=get_datas()[1])
    def test_add(self,get_calc,get_datas1):
        print('加法正确的测试用例')
        result = round(get_calc.add(get_datas1[0],get_datas1[1]),2)
        assert result==get_datas1[2]

    @pytest.mark.add
    @pytest.mark.run(order=1)
   # @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_add_wrong(self,get_calc,get_datas2):
        print('加法错误的测试用例')
        result = get_calc.add(get_datas2[0],get_datas2[1])
        assert not result==get_datas2[2]

    #减法测试用例
    @pytest.mark.sub
    @pytest.mark.run(order=3)
   # @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_sub(self,get_calc,get_datas3):
        print('减法正确的测试用例')
        result = round(get_calc.sub(get_datas3[0],get_datas3[1]),2)
        assert result==get_datas3[2]

    @pytest.mark.sub
    @pytest.mark.run(order=3)
   # @pytest.mark.parametrize('a,b,expect', get_datas()[6], ids=get_datas()[7])
    def test_sub_wrong(self,get_calc,get_datas4):
        print('减法错误的测试用例')
        result = get_calc.sub(get_datas4[0],get_datas4[1])
        assert not result==get_datas4[2]
    #
    # #乘法测试用例
    @pytest.mark.mul
    @pytest.mark.run(order=4)
    #@pytest.mark.parametrize('a,b,expect', get_datas()[8], ids=get_datas()[9])
    def test_mul(self,get_calc,get_datas5):
        print('乘法正确的测试用例')
        result = round(get_calc.mul(get_datas5[0],get_datas5[1]),2)
        assert result==get_datas5[2]

    @pytest.mark.mul
    @pytest.mark.run(order=4)
   # @pytest.mark.parametrize('a,b,expect', get_datas()[10], ids=get_datas()[11])
    def test_mul_wrong(self,get_calc,get_datas6):
        print('乘法错误的测试用例')
        result = get_calc.mul(get_datas6[0],get_datas6[1])
        assert not result==get_datas6[2]


    #除法测试用例
    @pytest.mark.div
    @pytest.mark.run(order=2)
   # @pytest.mark.parametrize('a,b,expect', get_datas()[12], ids=get_datas()[13])
    def test_div(self,get_calc,get_datas7):
        print('除法正确的测试用例')
        result = get_calc.div(get_datas7[0],get_datas7[1])
        assert result==get_datas7[2]

    @pytest.mark.run(order=2)
    #@pytest.mark.parametrize('a,b,expect', get_datas()[14], ids=get_datas()[15])
    def test_div_wrong(self,get_calc,get_datas8):
        print('除法错误的测试用例')
        result = get_calc.div(get_datas8[0],get_datas8[1])
        assert not result==get_datas8[2]
