package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.github.ontio.account.Account;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class ONG_Native {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		//OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
		//Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		System.out.println("setUp");
		OntTest.api().node().initOntOng();
		Thread.sleep(5000);
		System.out.println("setUp over");
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	/************************************************************************/
	@Test
	public void test_base_001_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//正确的sendAcct
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			//Account acc1 = OntTest.common().getAccount(0);
			Account acc1 = null;
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
			System.out.println(e);
			String ret_err = String.valueOf(e);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_004_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"abc";
			//recvAddr不存在（乱码但符合recvAddr34个字符要求）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_007_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr2 = "";
			//留空
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"address should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_010_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//正确的数量0
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_011_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//amount为负数
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			//amount大于实际所有的ONG数量
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);

			assertEquals(true,inc==0);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			Account payer = null;
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, payer, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_021_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = -20000;
			//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
			long gasprice = 0;
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_022_sendTransfer() throws Exception {
//		OntTest.logger().description("测试sendTransfer参数sendAcct");
//		
//		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			//错误的数量gaslimit为20000（实际步数大于20000但ONG足够）
//			long gasprice = 0;
//			
//			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			System.out.println("start:");
//			System.out.println(ongnum1);
//			System.out.println(ongnum2);
//			
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			System.out.println(Transfer);
//			Thread.sleep(5000);
//			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
//			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//			System.out.println("final:");
//			System.out.println(ongnum3);
//			System.out.println(ongnum4);			
//			
//			long dec = ongnum1-ongnum3;
//			long inc = ongnum4-ongnum2;
//			System.out.println(inc);
//			assertEquals(true,inc==1000000000);
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}

	@Test
	public void test_abnormal_027_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = -1000000;
			//错误的数量（负数）
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_028_sendTransfer() throws Exception {
		OntTest.logger().description("测试sendTransfer参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			long gaslimit = 20000;
			long gasprice = 1000000L;
			//错误的数量10（ONG小于gaslimit与gasprice的乘积加上amount）
			
			long ongnum1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("start:");
			System.out.println(ongnum1);
			System.out.println(ongnum2);
			
			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Transfer);
			Thread.sleep(5000);
			long ongnum3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			long ongnum4 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
			System.out.println("final:");
			System.out.println(ongnum3);
			System.out.println(ongnum4);			
			
			long dec = ongnum1-ongnum3;
			long inc = ongnum4-ongnum2;
			System.out.println(inc);
			assertEquals(true,inc==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_031_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			//正确的address值
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			System.out.println(ongnum);

			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_032_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			addr1 = addr1.substring(0,addr1.length()-3)+"abc";
			//address不存在，未创建的地址（34个字符）
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			System.out.println(ongnum);

			assertEquals(true,false);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_033_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = addr1+"a";
			//address长度为35及以上
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			System.out.println(ongnum);

			assertEquals(true,false);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_queryBalanceOf() throws Exception {
		OntTest.logger().description("测试queryBalanceOf参数address");
		
		try {
			//String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();	
			String addr1 = "";
			//留空
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			System.out.println(ongnum);

			assertEquals(true,true);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"address should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_base_035_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的fromAddr值
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_036_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//fromAddr存在，但并没有前提sendApprove
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_037_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			add1 = add1.substring(0,add1.length()-3)+"abc";
			//fromAddr不存在，未创建的地址（34个字符）
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_038_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			add1 = add1+"a";
			//fromAddr长度为35及以上
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_039_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			//String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add1 = "";
			//留空
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		}catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameter should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		}catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_040_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//fromAddr和toAddr与sendApprove时相反
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add2, add1);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();	
			//toAddr存在，但并没有前提sendApprove
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);
			long Allowance1 = Long.valueOf(OntTest.sdk().getRpc().getAllowance("ong",add1,add2));
			System.out.println(Allowance1);
			assertEquals(true,Allowance==Allowance1);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_043_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = add2.substring(0,add2.length()-3)+"abc";
			//toAddr不存在，未创建的地址（34个字符）
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_044_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = add2 +"a";
			//toAddr长度为35及以上
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_045_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			add2 = add2.substring(0,add2.length()-1);
			//toAddr长度为33及以下
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_046_queryAllowance() throws Exception {
		OntTest.logger().description("测试queryAllowance参数toAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			String add1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String add2 = OntTest.common().getAccount(1).getAddressU160().toBase58();	
			String add2 = "";
			//留空
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(add1, add2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameter should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_047_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的sendAcct（与payerAcct一致）
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_048_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			//Account acc1 = OntTest.common().getAccount(0);
			Account acc1 = null;
			//留空
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_050_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"abc";
			//recvAddr不存在（乱码但符合recvAddr34个字符要求）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_051_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2 + "a";
			//recvAddr长度为35及以上
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_052_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			addr2 = addr2.substring(0,addr2.length()-3)+"#@$";
			//34个字符的recvAddr中包含非法符号（%￥#）
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_053_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr2 = "";
			//留空
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_055_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//正确的数量0，sendAcct也有足够ONG
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//amount为负数，sendAcct也有足够ONG
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_059_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+10000000L;
			//amount大于实际所有的ONG数量
			long gaslimit = 20000;
			long gasprice = 0;
			
			long Allowance1 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println("Allowance1:"+Allowance1);
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance2 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println("Allowance2:"+Allowance2);

			assertEquals(true,Allowance1==Allowance2);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_062_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数payerAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, null, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(false,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_065_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = -20000;
			//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_067_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, 1L, acc1, 20000L, 0L);
			System.out.println("ONG = "+ OntTest.sdk().nativevm().ong().queryBalanceOf(addr1));
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+2000000000L;
			System.out.println("amount : "+amount);
			long gaslimit = 20000;
			//错误的数量20000，ONG小于gaslimit与gasprice的乘积加上amount
			long gasprice = 0L;
			
			long Allowance1 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println("Allowance1 : "+Allowance1);
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance2 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println("Allowance2 : "+Allowance2);

			assertEquals(true,amount==Allowance2);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_071_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = -10000;
			//正确的数量（负数）
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==1000000000);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_072_sendApprove() throws Exception {
		OntTest.logger().description("测试sendApprove参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1)+1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			//正确的数量10（ONG小于gaslimit与gasprice的乘积加上amount）
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance);

			assertEquals(true,Allowance==amount);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_075_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {	
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			//正确的sendAcct
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			System.out.println("amount = "+amount);
			long gaslimit = 20000;
			long gasprice = 0;
			
			long ongnum = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
			System.out.println("addr1 has "+ongnum+" ong");
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(8000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println("Allowance0 = "+Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, gasprice);
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_076_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc1, addr1, addr2, amount, acc2, gaslimit, gasprice);
				//sendAcct并非sendApprove的账户
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_077_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(null, addr1, addr2, amount, acc2, gaslimit, gasprice);
				//sendacct留空
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_079_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数fromAddr");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr3 = OntTest.common().getAccount(2).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr3, addr2, amount, acc2, gaslimit, gasprice);
				//fromAddr存在，但并非sendApprove的地址
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_082_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, "", addr2, amount, acc2, gaslimit, gasprice);
				//fromaddr留空
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_084_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			String addr3 = OntTest.common().getAccount(2).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr3, amount, acc2, gaslimit, gasprice);
				//toAddr存在，但并非sendApprove的地址
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_086_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2+"a", amount, acc2, gaslimit, gasprice);
				//toAddr长度为35及以上
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_087_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2.substring(0,addr2.length()-1), amount, acc2, gaslimit, gasprice);
				//toAddr长度为33及以下
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_088_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, "", amount, acc2, gaslimit, gasprice);
				//留空
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_090_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, 0L, acc2, gaslimit, gasprice);
				//正确的数量0
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==0);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_091_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, -100000L, acc2, gaslimit, gasprice);
				//amount为负数
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(false,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_092_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, Allowance0+1000000000L, acc2, gaslimit, gasprice);
				//amount大于Allowance中实际所有的ONG数量
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==0);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_094_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc3, gaslimit, gasprice);
				//payerAcct为第三方，与sendAcct不一致
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_095_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(8000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, null, gaslimit, gasprice);
				//payer留空
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_097_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数gaslimit");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, 0, gasprice);
				//gaslimit错误的数量0（但实际步数大于0小于20000且ONG足够）
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"Please input gasLimit >= 20000 and gasPrice >= 0\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_098_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, -20000L, gasprice);
				//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_099_sendTransferFrom() throws Exception {
//		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
//		
//		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//			
//			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			System.out.println(Approve);
//			Thread.sleep(5000);
//			
//			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
//			System.out.println(Allowance0);
//			if(Allowance0==1000000000) {
//				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
//				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, gasprice);
//				//错误的数量gaslimit为20000（实际步数大于20000但ONG足够）
//				System.out.println(TransferFrom);
//				Thread.sleep(5000);
//				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
//				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
//			}else {
//				System.out.println("Allowance与sendApprove的amount不一致");
//				assertEquals(true,false);
//			}
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}
	
	@Test
	public void test_abnormal_100_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.sdk().nativevm().ong().sendTransfer(acc2, addr1, ongnum_addr2, acc2, 20000L, 0L);
				Thread.sleep(5000);
				long ongnum_addr_should0 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2_should0 has "+ongnum_addr_should0+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, 1000000000L);
				//错误的数量20000，自身ONG小于gaslimit与gasprice的乘积
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"transactor 54297f32c6f9886921cd168fb246605d04bf1812 has no balance enough to cover gas cost 20000000000000\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
//	@Test
//	public void test_abnormal_101_sendTransferFrom() throws Exception {
//		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
//		
//		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			//错误的数量1000000000，sendAcct的ONG充足
//			long gasprice = 0;
//			
//			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			System.out.println(Approve);
//			Thread.sleep(5000);
//			
//			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
//			System.out.println(Allowance0);
//			if(Allowance0==1000000000) {
//				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
//				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, 1000000000, gasprice);
//				System.out.println(TransferFrom);
//				Thread.sleep(5000);
//				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
//				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
//				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
//			}else {
//				System.out.println("Allowance与sendApprove的amount不一致");
//				assertEquals(true,false);
//			}
//		} catch(Exception e) {
//			System.out.println(e);
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}
	
	@Test
	public void test_abnormal_103_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2 has "+ongnum_addr2+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, -100000L);
				//正确的数量（负数）
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_104_sendTransferFrom() throws Exception {
		OntTest.logger().description("测试sendTransferFrom参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1000000000;
			long gaslimit = 20000;
			long gasprice = 0;
			
			String Approve = OntTest.sdk().nativevm().ong().sendApprove(acc1, addr2, amount, acc1, gaslimit, gasprice);
			System.out.println(Approve);
			Thread.sleep(5000);
			
			long Allowance0 = OntTest.sdk().nativevm().ong().queryAllowance(addr1, addr2);
			System.out.println(Allowance0);
			if(Allowance0==1000000000) {
				long ongnum_addr2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				OntTest.sdk().nativevm().ong().sendTransfer(acc2, addr1, ongnum_addr2, acc2, 20000L, 0L);
				Thread.sleep(5000);
				long ongnum_addr_should0 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("start : addr2_should0 has "+ongnum_addr_should0+" ong");
				String TransferFrom = OntTest.sdk().nativevm().ong().sendTransferFrom(acc2, addr1, addr2, amount, acc2, gaslimit, 1000000000L);
				//错误的数量10（自身ONG小于gaslimit与gasprice的乘积）
				System.out.println(TransferFrom);
				Thread.sleep(5000);
				long ongnum_addr3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr2);
				System.out.println("final : addr2 has "+ongnum_addr3+" ong");
				assertEquals(true,(ongnum_addr3-ongnum_addr2)==1000000000);
			}else {
				System.out.println("Allowance与sendApprove的amount不一致");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"transactor 54297f32c6f9886921cd168fb246605d04bf1812 has no balance enough to cover gas cost 20000000000000\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_106_queryName() throws Exception {
		OntTest.logger().description("测试queryName");
		
		try {
			String ret = OntTest.sdk().nativevm().ong().queryName();
			System.out.println(ret);
			String exp = "ONG Token";
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_107_querySymbol() throws Exception {
		OntTest.logger().description("测试querySymbol");
		
		try {
			String ret = OntTest.sdk().nativevm().ong().querySymbol();
			System.out.println(ret);
			String exp = "ONG";
			assertEquals(true,ret.equals(exp));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_108_queryDecimals() throws Exception {
		OntTest.logger().description("测试queryDecimals");
		
		try {
			long ret = OntTest.sdk().nativevm().ong().queryDecimals();
			System.out.println(ret);
			long exp = 9;
			assertEquals(true,ret==exp);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_109_queryTotalSupply() throws Exception {
		OntTest.logger().description("测试queryTotalSupply");
		
		try {
			long ret = OntTest.sdk().nativevm().ong().queryTotalSupply();
			System.out.println(ret);
			long exp = 1000000000000000000L;
			assertEquals(true,ret==exp);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_110_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			//正确的sendAcct
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_111_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(null, addr1, amount, acc1, gaslimit, gasprice);
				//留空
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_113_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1.substring(0,addr1.length()-3)+"abc", amount, acc1, gaslimit, gasprice);
				//toAddr不存在（乱码但符合toAddr34个字符要求）
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_114_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1 ,addr1+"a", amount, acc1, gaslimit, gasprice);
				//toAddr长度为35及以上
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_115_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();

			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1.substring(0,addr1.length()-3)+"@#$", amount, acc1, gaslimit, gasprice);
				//34个字符的toAddr中包含非法符号（%￥#）
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_116_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,"", amount, acc1, gaslimit, gasprice);
				//留空
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_118_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 0;
			//错误的数量0
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gaslimit gasprice should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_119_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = -1000000000;
			//正确的数量（负数）
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				System.out.println(withdrawOng);
				assertEquals(true,true);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gaslimit gasprice should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_120_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);

			//错误的数量（超出未提取的ONG数量）
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			long amount = ongnum+100000000L;
			System.out.println(amount);
			
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==0);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gaslimit gasprice should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_121_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//正确的payerAcct
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==0);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_122_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc2, gaslimit, gasprice);
				//payerAcct与sendAcct不一致，payerAcct为第三方
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==0);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_123_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, null, gaslimit, gasprice);
				//留空
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_126_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = -20000;
			long gasprice = 0;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start : "+addr1_Ong1);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//正确的数量gaslimit为负数（实际步数小于20000且ONG足够）
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong2);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gaslimit gasprice should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_128_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 100000L;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, addr1_Ong1, acc1, gaslimit, gasprice);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start(should be 0) : "+addr1_Ong2);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//错误的数量20000，自身ONG小于gaslimit与gasprice的乘积
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong3);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"transactor 92b47e409e3462335afd2f82def0a8d717062b04 has no balance enough to cover gas cost 2000000000\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_131_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = -100000L;
			//正确的数量（负数）

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1, addr1, amount, acc1, gaslimit, gasprice);
				System.out.println(withdrawOng);
				assertEquals(true,false);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gaslimit gasprice should not be less than 0\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_132_claimOng() throws Exception {
		OntTest.logger().description("测试claimOng参数sendAcct");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
			 
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			long amount = 1;
			long gaslimit = 20000;
			long gasprice = 100000L;

//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);
			if(ongnum>1) {
				long addr1_Ong1 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, addr1_Ong1, acc1, gaslimit, gasprice);
				Thread.sleep(5000);
				long addr1_Ong2 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("start(should be 0) : "+addr1_Ong2);
				String withdrawOng = OntTest.sdk().nativevm().ong().withdrawOng(acc1,addr1, amount, acc1, gaslimit, gasprice);
				//错误的数量10（自身ONG小于gaslimit与gasprice的乘积）
				System.out.println(withdrawOng);
				Thread.sleep(5000);
				long addr1_Ong3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr1);
				System.out.println("final : "+addr1_Ong3);
				
				assertEquals(true,(addr1_Ong2-addr1_Ong1)==1);
			}else {
				System.out.println("可提取的ong数量不足");
				assertEquals(true,false);
			}
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"transactor 92b47e409e3462335afd2f82def0a8d717062b04 has no balance enough to cover gas cost 2000000000\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_134_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//正确的address值
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);

			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_135_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = addr1.substring(0,addr1.length()-3)+"abc";
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//address不存在，未创建的地址（34个字符）
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);

			assertEquals(true,false);
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"\",\"id\":1,\"error\":42002,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID PARAMS\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_136_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
			addr1 = addr1 + "a";
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng(addr1);
			//address长度为35及以上
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);

			assertEquals(true,true);
		} catch(RpcException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.network.exception.RpcException: {\"result\":\"\",\"id\":1,\"error\":42002,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID PARAMS\"}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_137_unclaimOng() throws Exception {
		OntTest.logger().description("测试unclaimOng参数address");
		
		try {
//			String addr1 = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String addr2 = OntTest.common().getAccount(1).getAddressU160().toBase58();
//			 
//			Account acc1 = OntTest.common().getAccount(0);
//			Account acc2 = OntTest.common().getAccount(1);
//			long amount = 1000000000;
//			long gaslimit = 20000;
//			long gasprice = 0;
//
//			String Transfer = OntTest.sdk().nativevm().ong().sendTransfer(acc1, addr2, amount, acc1, gaslimit, gasprice);
//			Thread.sleep(5000);
			
			String unboundOng = OntTest.sdk().nativevm().ong().unboundOng("");
			//留空
			long ongnum = Long.valueOf(unboundOng);
			System.out.println(ongnum);

			assertEquals(true,true);
		} catch(SDKException e) {
			String ret_err = String.valueOf(e);
			System.out.println(ret_err);
			String exp_err = String.valueOf("com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"address should not be null\",\"Error\":58005}");
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
}
