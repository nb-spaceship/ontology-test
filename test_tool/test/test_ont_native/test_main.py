# -*- coding:utf-8 -*-

import ddt
import unittest
import urllib
import urllib.request
import json
import os
import sys, getopt
import time 

sys.path.append('..')
sys.path.append('../..')

from utils.config import Config
from utils.taskdata import TaskData, Task
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.parametrizedtestcase import ParametrizedTestCase
from api.apimanager import API
from test_api import *

testpath = os.path.dirname(os.path.realpath(__file__))

node_index=5
nodePath=Config.NODE_PATH
contract_address=API.contract().deploy_contract(testpath + "/ont_neo.json")
pay_address=Config.NODES[node_index]["address"]
get_address=Config.NODES[2]["address"]
amount="10"
sender=Config.NODES[2]["address"]
sender_node=2
senderType=False

##############################
from1= pay_address  #from_正确的from值_正常
from2= "1111111111111111111111111111"  #from_错误的from值（参数不正确）_异常
from3= ""  #from_留空_异常
to1= get_address  #to_正确的to值_正常
to2= from2  #to_错误的to值_异常
to3= ""  #to_留空_异常
amount1= "10"  #amount_正确的数量10_正常
amount2= "0"  #amount_正确的数量0_正常
amount3= "-1"  #amount_错误的数量（-1）_异常
amount4= "2000000000000"  #amount_错误的数量（from账户不存在这么多数量的ont）_异常
amount5= "abc"  #amount_错误的数量（abc）_异常
amount6= ""  #amount_错误的数量（留空）_异常
from4= from2  #from_错误的from值_异常
sender1= to1 #sender_正确的sender值（被授权的账户地址)_正常
sender1_node=2
sender1Type=senderType
sender2= contract_address  #sender_正确的sender值（被授权的智能合约地址)_正常
sender2_node=2
sender2Type=True
sender3= from1  #sender_正确的sender值（from账户地址)_正常
sender3_node=2
sender3Type=False
sender4= "ANdtbPPwfMv79eMev9z7aAZRM6bUuQQ3rf"  #sender_错误的sender值（未被授权的账户地址)_异常
sender4_node=2
sender4Type=False
sender5= API.contract().deploy_contract(testpath + "/ontErr.json")  #sender_错误的sender值（未被授权的智能合约地址)_异常
sender5_node=2
sender5Type=True
sender6= "abc"  #sender_错误的sender值（abc）_异常
sender6Type=False
sender6_node=2
sender7= ""  #sender_留空_异常
sender7_node=2
sender7Type=False
from5= from1  #from_正确的from值（账户存在）_正常
from6= "ASK6GGsZfPf8WfSYhWUhw7SaZxnZ111111"  #from_错误的from值（账户不存在）_异常
to4= to1  #to_正确的to值（账户存在）_正常
to5= from6  #to_错误的to值（账户不存在）_异常
amount7= "10"  #amount_正确的数量10_异常
address1= from1  #address_正确的address值_正常
address2= from2  #address_错误的address值_异常
address3= ""  #address_留空_异常
from7= from1  #from_正确的from值_异常
sender8= to1  #sender_正确的sender值（被授权的账户地址)_异常
sender8_node=5
sender8Type=False
address4= from1  #address_正确的address值_异常

####################################################
#test cases
class test_ont_native_1(ParametrizedTestCase):
	def test_init(self):
		API.node().stop_all_nodes()
		API.node().start_nodes(range(0, 7), Config.DEFAULT_NODE_ARGS, clear_chain = True, clear_log = True)
		time.sleep(10)
		API.native().init_ont_ong()
		time.sleep(10)
		global contract_address
		contract_address=API.contract().deploy_contract(testpath + "/ont_neo.json")
		global sender5
		sender5= API.contract().deploy_contract(testpath + "/ontErr.json") 
		#os.system(nodePath+ "/ontology account import -s wallettest.dat -w "+nodePath+"/wallet.dat")
		#deploy_contract
		
	def setUp(self):
		logger.open( self._testMethodName+".log",self._testMethodName)
		
	def tearDown(self):
		logger.close(self.m_result)
	
	def test_base_001_transfer(self):
		try:
			(process, response) = transfer(contract_address,from1,get_address,amount, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
		
	def test_abnormal_002_transfer(self):
		try:
			(process, response) = transfer(contract_address,from2,get_address,amount, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_003_transfer(self):
		try:
			(process, response) = transfer(contract_address,from3,get_address,amount, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_004_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,to1,amount, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_005_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,to2,amount, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_006_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,to3,amount, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_007_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,get_address,amount1, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_008_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,get_address,amount2, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_009_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,get_address,amount3, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_010_transfer(self):
		try:
			(process, response) = transfer(contract_address,pay_address,get_address,amount4, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_013_approve(self):
		try:
			(process, response) = approve(contract_address,from1,get_address, amount,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_014_approve(self):
		try:
			(process, response) = approve(contract_address,from4,get_address, amount,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_015_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,to1, amount,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)	


	def test_normal_016_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,to2, amount,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)	


	def test_normal_017_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,get_address, amount1,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_018_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,get_address, amount2,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_019_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,get_address, amount4,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_020_approve(self):
		try:
			(process, response) = approve(contract_address,pay_address,get_address, amount3,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_023_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
			time.sleep(15)
			(process, response) = transferFrom(contract_address,sender1,pay_address,get_address, amount,2,sender1Type,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

		
	def test_normal_024_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,contract_address, amount,node_index,0)#先approve
			time.sleep(15)
			(process, response) = transferFrom(contract_address,sender2,pay_address,contract_address, amount,sender2_node,sender2Type,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_025_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)#先approve
			time.sleep(15)
			(process, response) = transferFrom(contract_address,sender3,pay_address,get_address, amount,sender3_node,sender3Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_026_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender4,pay_address,get_address, amount,sender4_node,sender4Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_027_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender5,pay_address,get_address, amount,sender5_node,sender5Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_028_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender6,pay_address,get_address, amount,sender6_node,sender6Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_029_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender7,pay_address,get_address, amount,sender7_node,sender7Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_030_transferFrom(self):
		try:
			(proces, response) = approve1(contract_address,from5,get_address, amount,node_index,0)#先approve
			time.sleep(15)
			(proces, response) = transferFrom(contract_address,sender,from5,get_address, amount,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)



	def test_abnormal_031_transferFrom(self):
		try:
			(proces, response) = transferFrom(contract_address,sender,from6,get_address, amount,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_032_transferFrom(self):
		try:
			#(process, response) = approve1(contract_address,from3,get_address, amount,node_index,0)#先approve
			(process, response) = transferFrom(contract_address,sender,from3,get_address, amount,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_033_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to4, amount,node_index,0)#先approve
			(process, response) = transferFrom(contract_address,sender,pay_address,to4, amount,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)



	def test_abnormal_034_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender,pay_address,to5, amount,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)



	def test_abnormal_035_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender,pay_address,to3, amount,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_036_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
			(process, response) = transferFrom(contract_address,sender,pay_address,get_address, amount1,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)



	def test_normal_037_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
			(process, response) = transferFrom(contract_address,sender,pay_address,get_address, amount2,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_038_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender,pay_address,get_address, amount4,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)



	def test_abnormal_039_transferFrom(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, "1",node_index,0)
			(process, response) = transferFrom(contract_address,sender,pay_address,get_address, amount7,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_040_transferFrom(self):
		try:
			(process, response) = transferFrom(contract_address,sender,pay_address,get_address, amount3,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_043_name(self):
		try:
			(process, response) = name(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_044_symbol(self):
		try:
			(process, response) = symbol(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_045_decimals(self):
		try:
			(process, response) = decimals(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_046_totalSupply(self):
		try:
			(process, response) = totalSupply(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_047_balanceOf(self):
		try:
			(process, response) = balanceOf(contract_address,address1,node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_048_balanceOf(self):
		try:
			(process, response) = balanceOf(contract_address,address2,node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_049_balanceOf(self):
		try:
			(process, response) = balanceOf(contract_address,address3,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_050_allowance(self):
		try:
			(process, response) = approve1(contract_address,from1,get_address, amount,node_index,0)#先approve
			(process, response) = allowance(contract_address,from1,get_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_051_allowance(self):
		try:
			(process, response) = allowance(contract_address,from4,get_address,node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_052_allowance(self):
		try:
			(process, response) = allowance(contract_address,from3,get_address,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_normal_053_allowance(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)#先approve
			(process, response) = allowance(contract_address,pay_address,to1,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_054_allowance(self):
		try:
			(process, response) =allowance(contract_address,pay_address,to2,node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_055_allowance(self):
		try:
			(process, response) = allowance(contract_address,pay_address,to3,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_056_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,from1,get_address,amount, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_057_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,from2,get_address,amount, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_058_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,from3,get_address,amount, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_059_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,to1,amount, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

	def test_abnormal_060_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,to2,amount, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_061_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,to3,amount, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_062_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount1, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_063_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount2, node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_064_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount3, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_065_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount4, node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_066_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount5, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_067_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,pay_address,get_address,amount6, node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_068_approve1(self):
		try:
			(process, response) = approve1(contract_address,from1,get_address, amount,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_069_approve1(self):
		try:
			(process, response) = approve1(contract_address,from4,get_address, amount,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_070_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_071_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to2, amount,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_072_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount1,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_073_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount2,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_074_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount4,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_075_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount3,node_index)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_076_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount5,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_077_approve1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount6,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_078_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
			time.sleep(15)
			(process, response) = transferFrom1(contract_address,sender1,pay_address,get_address, amount,sender1_node,sender1Type,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_079_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount,node_index,0)
			time.sleep(15)
			(process, response) = transferFrom1(contract_address,sender2,pay_address,get_address, amount,sender2_node,sender2Type,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_080_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,contract_address, amount,node_index,0)
			time.sleep(15)
			(process, response) = transferFrom1(contract_address,sender3,pay_address,contract_address, amount,sender3_node,sender3Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_081_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender4,pay_address,get_address, amount,sender4_node,sender4Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_082_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender5,pay_address,get_address, amount,sender5_node,sender5Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_083_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender6,pay_address,get_address, amount,sender6_node,sender6Type,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_084_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender7,pay_address,get_address, amount,sender7_node,sender7Type,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_085_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,from5,get_address, amount,node_index,0)

			(process, response) = transferFrom1(contract_address,sender,from5,get_address, amount,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_086_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,from6,get_address, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_087_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,from3,get_address, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_088_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to4, amount,node_index,0)

			(process, response) = transferFrom1(contract_address,sender,pay_address,to4, amount,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_089_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,to5, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_090_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,to3, amount,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_091_transferFrom1(self):
		try:

			(process, response) = approve1(contract_address,pay_address,get_address, amount1,node_index,0)
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount1,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_092_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, amount2,node_index,0)

			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount2,sender_node,senderType,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_093_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount4,node_index,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_094_transferFrom1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,get_address, "0",node_index,0)
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount7,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_095_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount3,sender_node,senderType)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_096_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount5,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_097_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender,pay_address,get_address, amount6,sender_node,senderType,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_098_name1(self):
		try:
			(process, response) = name1(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_099_symbol1(self):
		try:
			(process, response) = symbol1(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_100_decimals1(self):
		try:
			(process, response) = decimals1(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_101_totalSupply1(self):
		try:
			(process, response) = totalSupply1(contract_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_base_102_balanceOf1(self):
		try:
			(process, response) = balanceOf1(contract_address,address1,node_index,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_103_balanceOf1(self):
		try:
			(process, response) = balanceOf1(contract_address,address2,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_104_balanceOf1(self):
		try:
			(process, response) = balanceOf1(contract_address,address3,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)

######################################
	def test_base_105_allowance1(self):
		try:
			(process, response) = approve1(contract_address,from1,get_address, amount,node_index,0)

			(process, response) = allowance1(contract_address,from1,get_address,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_106_allowance1(self):
		try:
			(process, response) = allowance1(contract_address,from4,get_address,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_107_allowance1(self):
		try:
			(process, response) = allowance1(contract_address,from3,get_address,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_normal_108_allowance1(self):
		try:
			(process, response) = approve1(contract_address,pay_address,to1, amount,node_index,0)

			(process, response) = allowance1(contract_address,pay_address,to1,node_index,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_109_allowance1(self):
		try:
			(process, response) = allowance1(contract_address,pay_address,to2,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_110_allowance1(self):
		try:
			(process, response) = allowance1(contract_address,pay_address,to3,node_index,errorcode=900,errorkey="error_code")
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_111_transfer1(self):
		try:
			(process, response) = transfer1(contract_address,from7,get_address,amount, 0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_112_approve1(self):
		try:
			(process, response) = approve1(contract_address,from7,get_address, amount,0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_113_transferFrom1(self):
		try:
			(process, response) = transferFrom1(contract_address,sender8,pay_address,get_address, amount,0,sender8Type)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_114_balanceOf1(self):
		try:
			(process, response) = balanceOf1(contract_address,address4,0,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)


	def test_abnormal_115_allowance1(self):
		try:
			(process, response) = allowance1(contract_address,pay_address,get_address,0,errorcode=0)
			self.ASSERT(process, "")
		except Exception as e:
			print(e.args)
		

####################################################
if __name__ == '__main__':
	unittest.main()

