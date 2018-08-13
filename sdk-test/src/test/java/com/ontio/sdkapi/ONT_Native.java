package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.github.ontio.account.Account;
import com.github.ontio.common.Helper;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class ONT_Native {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
//		OntTest.api().node().initOntOng();
//		OntTest.api().node().restartAll("ontology", "test_config.json", Config.DEFAULT_NODE_ARGS);
		Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	@Test
	public void test_base_001_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 1000L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
			}
			else {
				System.out.println("转账失败！");
			}
		} 
		catch(SDKException e) {
			System.out.println(e.toString());
			assertEquals(true,true);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_002_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(null, addr2, 1000L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
			}
			else {
				System.out.println("转账失败！");
			}
		} 
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_004_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			Account acc3 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String addr3 = acc3.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			System.out.println(addr3);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long before_bala3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr3);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			System.out.println("账户3 的ong余额为"+before_bala3);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 1000L, acc3, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			long after_bala3 = OntTest.sdk().nativevm().ong().queryBalanceOf(addr3);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			System.out.println("账户3 的ong余额为"+after_bala3);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0 && before_bala3 - after_bala3 > 0) {
				System.out.println("转账成功！");
			}
			else {
				System.out.println("转账失败！");
			}
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_006_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, "", 1000L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
			}
			else {
				System.out.println("转账失败！");
			}
		} 
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_008_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 0, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
			}
			else {
				System.out.println("转账失败！");
			}
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		 catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_abnormal_009_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, -2000L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
		}
	
	
	@Test
	public void test_abnormal_011_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10000000000L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	@Test
	public void test_normal_013_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	@Test
	public void test_abnormal_014_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, null, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_abnormal_017_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, -2000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_020_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, 10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
		
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	
	@Test
	public void test_abnormal_021_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100L, acc1, 20000L, -10L);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_022_sendTransfer() throws Exception {
		OntTest.logger().description("----------sendTransfer----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			System.out.println(addr1);
			System.out.println(addr2);
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			String ts = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 1);
			System.out.println(ts);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("转账成功！");
				}
			else {
				System.out.println("转账失败！");
				}
			} 
		catch(RpcException e) {
			System.out.println(e.toString());
			assertEquals(false ,false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_023_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			
			String addr1 = acc1.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			System.out.println(l);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_025_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("AbwJsJYQPBSw67SVP7hctkWsfzgikwNkvh");
			System.out.println(l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_026_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("AbwJsJYQPBSw%&#SVP7hctkWsfzgikwNkv");
			System.out.println(l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_027_queryBalanceOf() throws Exception {
		OntTest.logger().description("----------queryBalanceOf----------");
		
		try {
			
			long l = OntTest.sdk().nativevm().ont().queryBalanceOf("");
			System.out.println(l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"address should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_028_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println("queryAllowance:"+l);
			if(l == 10) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_029_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(2);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1,addr2 );
			System.out.println("queryAllowance:"+l);
			
			if(l == 0) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_031_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
	
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1+"G", addr2);
			System.out.println("queryAllowance:"+l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_032_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance("Af296@#$TqHV5byLvXdCWCheW3HcpMpcNa", addr2);
			System.out.println("queryAllowance:"+l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_033_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
	
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr2, addr1);
			System.out.println("queryAllowance:"+l);
			if(l == 0) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_034_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance("" , addr2);
			System.out.println("queryAllowance:"+l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameter should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_036_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(2);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1,addr2);
			System.out.println("queryAllowance:"+l);
			
			if(l == 0) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_038_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , addr2+"G");
			System.out.println("queryAllowance:"+l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_039_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.logger().step("1.调用sendapprove");
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , "AKv$%^sbk3ucmTHHg9hPK3kehoQHG5g9CG");
			System.out.println("queryAllowance:"+l);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_040_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			OntTest.logger().step("2.调用queryAllowance");
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr2 , addr1);
			System.out.println("queryAllowance:"+l);
			
			if(l == 0) {
			System.out.println("成功！");
		}
		else{
			System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_041_queryAllowance() throws Exception {
		OntTest.logger().description("----------queryAllowance----------");
		try {
			Account acc1 = OntTest.common().getAccount(1);
			Account acc2 = OntTest.common().getAccount(2);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1 , "");
			System.out.println("queryAllowance:"+l);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameter should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_042_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println("sendApprove:"+l);
			
			if(l == 10) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_043_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(null, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_046_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2+"G", 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_048_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, "AKvRbmbk3ucmTHHg9hPK3kehoQHG5g%^&", 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_049_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, "", 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	

	@Test
	public void test_normal_050_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 20000L, 10L);
			Thread.sleep(5000);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println("sendApprove:"+l);
			
			if(l == 10) {
				System.out.println("成功！");
			}
			else{
				System.out.println("失败！");
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_051_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 0, 10L);
			Thread.sleep(5000);
			long l = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println("sendApprove:"+l);
			
		}
		catch(RpcException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.network.exception.RpcException: {\"result\":\"Please input gasLimit >= 20000 and gasPrice >= 0\",\"id\":1,\"error\":43001,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID TRANSACTION\"}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_054_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 50000L, acc1, 20000L, 1L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println("sendApprove:"+s);
		}
		catch(RpcException e) {
			System.out.println(e.toString());
			assertEquals(false, false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, null, 20000L, 0L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_059_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, -20000L, 1L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
		
	
	@Test
	public void test_abnormal_065_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 20000L, -1L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_066_sendApprove() throws Exception {
		OntTest.logger().description("----------sendApprove----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 10000L, acc1, 200000L, 1000L);
			Thread.sleep(5000);
			long s = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(s);
		}
		catch(RpcException e) {
			System.out.println(e.toString());
			assertEquals(false, false);
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_068_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_069_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(null, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_070_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc1, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_073_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_077_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr2, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_078_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, "", addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
	}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_080_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_082_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2+"F", 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"param error,\",\"Error\":58004}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_083_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, "AKv#$%sbk3ucmTHHg9hPK3kehoQHG5g9CG", 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_084_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr1, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_085_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, "", 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_087_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 0, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 >= 0 && after_bala2 - before_bala2 >= 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_088_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, -100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_090_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_091_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_092_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, null, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"parameters should not be null\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_095_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, -20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_098_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_100_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, -10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(SDKException e) {
			System.out.println(e.toString());
			String exp="com.github.ontio.sdk.exception.SDKException: {\"Desc\":\"amount or gasprice or gaslimit should not be less than 0\",\"Error\":58005}";
			assertEquals(true,e.toString().equals(exp));
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_101_sendTransferFrom() throws Exception {
		OntTest.logger().description("----------sendTransferFrom----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr2 = acc2.getAddressU160().toBase58();
			
			long before_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long before_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+before_bala1);
			System.out.println("账户2 的余额为"+before_bala2);
			
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100L, acc1, 20000, 10);
			Thread.sleep(5000);
			OntTest.sdk().nativevm().ont().sendTransferFrom(acc2, addr1, addr2, 100L, acc2, 20000L, 10L);
			Thread.sleep(5000);
			
			long after_bala1 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr1);
			long after_bala2 = OntTest.sdk().nativevm().ont().queryBalanceOf(addr2);
			System.out.println("账户1 的余额为"+after_bala1);
			System.out.println("账户2 的余额为"+after_bala2);
			
			if(before_bala1 - after_bala1 > 0 && after_bala2 - before_bala2 > 0) {
				System.out.println("成功！");
			}
			else {
				System.out.println("失败！");
			}
			
		}
		catch(RpcException e) {
			System.out.println(e.toString());
			assertEquals(false, false);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_102_queryName() throws Exception {
			
		OntTest.logger().description("----------queryName----------");
			
		try {
			String acc = OntTest.sdk().nativevm().ont().queryName();
			System.out.println(acc);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
		}
	
	@Test
	public void test_base_103_querySymbol() throws Exception {
			
		OntTest.logger().description("----------querySymbol----------");
			
		try {
			String acc = OntTest.sdk().nativevm().ont().querySymbol();
			System.out.println(acc);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_base_104_queryDecimals() throws Exception {
			
		OntTest.logger().description("----------queryDecimals----------");
			
		try {
			long acc = OntTest.sdk().nativevm().ont().queryDecimals();
			System.out.println(acc);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	@Test
	public void test_base_105_queryTotalSupply() throws Exception {
			
		OntTest.logger().description("----------queryTotalSupply----------");
			
		try {
			long acc = OntTest.sdk().nativevm().ont().queryTotalSupply();
			System.out.println(acc);
			} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
			}
	}
	
	
	
}
