# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt

sys.path.append('..')

from utils.config import Config

class test_config():
	node_index=5
	contract_address=""
	pay_address=Config.NODES[node_index]["address"]
	get_address=Config.NODES[2]["address"]
	amount="10"
	sender=Config.NODES[2]["address"]
	sender_node=2
	senderType=False
	
	from1= pay_address  #from_��ȷ��fromֵ_����
	from2= "1111111111111111111111111111"  #from_�����fromֵ����������ȷ��_�쳣
	from3= ""  #from_���_�쳣
	to1= get_address  #to_��ȷ��toֵ_����
	to2= from2  #to_�����toֵ_�쳣
	to3= ""  #to_���_�쳣
	amount1= "10"  #amount_��ȷ������10_����
	amount2= "0"  #amount_��ȷ������0_����
	amount3= "-1"  #amount_�����������-1��_�쳣
	amount4= "2000000000000"  #amount_�����������from�˻���������ô��������ont��_�쳣
	amount5= "abc"  #amount_�����������abc��_�쳣
	amount6= ""  #amount_�������������գ�_�쳣
	from4= from2  #from_�����fromֵ_�쳣
	sender1= to1 #sender_��ȷ��senderֵ������Ȩ���˻���ַ)_����
	sender1_node=2
	sender1Type=senderType
	sender2= ""  #sender_��ȷ��senderֵ������Ȩ�����ܺ�Լ��ַ)_����
	sender2_node=2
	sender2Type=True
	sender3= from1  #sender_��ȷ��senderֵ��from�˻���ַ)_����
	sender3_node=2
	sender3Type=False
	sender4= "ANdtbPPwfMv79eMev9z7aAZRM6bUuQQ3rf"  #sender_�����senderֵ��δ����Ȩ���˻���ַ)_�쳣
	sender4_node=2
	sender4Type=False
	sender5= ""  #sender_�����senderֵ��δ����Ȩ�����ܺ�Լ��ַ)_�쳣
	sender5_node=2
	sender5Type=True
	sender6= "abc"  #sender_�����senderֵ��abc��_�쳣
	sender6Type=False
	sender6_node=2
	sender7= ""  #sender_���_�쳣
	sender7_node=2
	sender7Type=False
	from5= from1  #from_��ȷ��fromֵ���˻����ڣ�_����
	from6= "ASK6GGsZfPf8WfSYhWUhw7SaZxnZ111111"  #from_�����fromֵ���˻������ڣ�_�쳣
	to4= to1  #to_��ȷ��toֵ���˻����ڣ�_����
	to5= from6  #to_�����toֵ���˻������ڣ�_�쳣
	amount7= "10"  #amount_��ȷ������10_�쳣
	address1= from1  #address_��ȷ��addressֵ_����
	address2= from2  #address_�����addressֵ_�쳣
	address3= ""  #address_���_�쳣
	from7= from1  #from_��ȷ��fromֵ_�쳣
	sender8= to1  #sender_��ȷ��senderֵ������Ȩ���˻���ַ)_�쳣
	sender8_node=5
	sender8Type=False
	address4= from1  #address_��ȷ��addressֵ_�쳣