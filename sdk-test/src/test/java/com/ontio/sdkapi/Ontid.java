package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.security.PrivateKey;
import java.util.Base64;
import java.util.Map;
import java.util.jar.Attributes;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.alibaba.fastjson.JSON;
import com.github.ontio.account.Account;
import com.github.ontio.core.ontid.Attribute;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.wallet.Identity;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class Ontid {

	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
//		OntTest.api().node().restartAll("ontology", "test_config.json", Config.DEFAULT_NODE_ARGS);
//		Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	
	
	@Test
	public void test_base_001_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 1, false);
			System.out.println(sr);
			assertEquals(true, true);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_002_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(null, "123456", acc1, 20000, 1, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_003_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 1, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_004_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "654321", acc1, 20000, 1, false);

			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_005_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "", acc1, 20000, 0, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_006_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("@#$%^&");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "@#$%^&", acc1, 20000, 0, false);
			System.out.println(sr);
			assertEquals(true, true);
			
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_007_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("Af296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3"
					+ "HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpc"
					+ "NaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296"
					+ "@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqH"
					+ "V5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLv"
					+ "XdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWChe"
					+ "W3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpM"
					+ "pcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf2"
					+ "96@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$Tq"
					+ "HV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLv"
					+ "XdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWChe"
					+ "W3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpc"
					+ "NaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@"
					+ "#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5b"
					+ "yLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWC"
					+ "heW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpM"
					+ "pcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf29"
					+ "6@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV"
					+ "5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNa");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "Af296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdC"
					+ "WCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3"
					+ "HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpc"
					+ "NaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf29"
					+ "6@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$Tq"
					+ "HV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLv"
					+ "XdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWChe"
					+ "W3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMp"
					+ "cNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf29"
					+ "6@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV"
					+ "5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdC"
					+ "WCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3Hc"
					+ "pMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf"
					+ "296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqH"
					+ "V5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXd"
					+ "CWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3Hc"
					+ "pMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf2"
					+ "96@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV"
					+ "5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNa", acc1, 20000, 1, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_008_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 1, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_009_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", null, 20000, 1, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_010_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 40000, 1, false);
			System.out.println(sr);
			assertEquals(true, true);
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_011_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 0, 1, false);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_012_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, -20000, 1, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_013_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
//			Account acc1 = OntTest.common().getAccount(0);
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 1, false);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_014_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 1000000000, 1000000000, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_016_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 10, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnormal_017_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, -10, false);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 10, false);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_019_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 1000000000, 10, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_020_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 10, false);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_021_sendRegister() throws Exception {
		OntTest.logger().description("----------sendRegister----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");
			String ontid1 = ci.ontid;
			Identity id1 = OntTest.sdk().getWalletMgr().getWallet().getIdentity(ontid1);
			String sr = OntTest.sdk().nativevm().ontId().sendRegister(id1, "123456", acc1, 20000, 10, true);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_022_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_023_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcA", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_abnormal_024_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN1", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_025_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("did:ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpc", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_026_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("did:ont:Af296avw#$qHV5byLvXdCWCheW3HcpMpcN", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_027_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("did:Af296avwQTqHV5byLvXdCWCheW3HcpMpcN", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_028_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("ont:Af296avwQTqHV5byLvXdCWCheW3HcpMpcA", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58004".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_029_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes("", "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_normal_030_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_031_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "654321", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_032_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("!@#$%^");
			String addr1 = acc.address;
			byte[] salt = acc.getSalt();
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "!@#$%^");
			String ontid = "did:ont:"+acc.address;
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "!@#$%^", salt, atr, acc1, 20000L, 0l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_033_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("Af296@#$TqHV5byLvXdCWCheW3HcpMpcN"
					+ "aAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@"
					+ "#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV"
					+ "5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXd"
					+ "CWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3"
					+ "HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNa"
					+ "Af296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$"
					+ "TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byL"
					+ "vXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWChe"
					+ "W3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcN"
					+ "aAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#"
					+ "$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byL"
					+ "vXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3"
					+ "HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf"
					+ "296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV"
					+ "5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWC"
					+ "heW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcN"
					+ "aAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$Tq"
					+ "HV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNa");
			String addr1 = acc.address;
			byte[] salt = acc.getSalt();
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "Af296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3Hc"
					+ "pMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@"
					+ "#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvX"
					+ "dCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpM"
					+ "pcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$"
					+ "TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdC"
					+ "WCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpc"
					+ "NaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$Tq"
					+ "HV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWC"
					+ "heW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaA"
					+ "f296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5"
					+ "byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW"
					+ "3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf2"
					+ "96@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5by"
					+ "LvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3Hc"
					+ "pMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@"
					+ "#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvX"
					+ "dCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMp"
					+ "cNa");
			String ontid = "did:ont:"+acc.address;

			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "Af296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLv"
					+ "XdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3"
					+ "HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaA"
					+ "f296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqH"
					+ "V5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCW"
					+ "CheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMp"
					+ "cNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#"
					+ "$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLv"
					+ "XdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3Hc"
					+ "pMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf29"
					+ "6@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5b"
					+ "yLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWChe"
					+ "W3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcN"
					+ "aAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$T"
					+ "qHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdC"
					+ "WCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpc"
					+ "NaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$"
					+ "TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNaAf296@#$TqHV5byLvXd"
					+ "CWCheW3HcpMpcNaAf296@#$TqHV5byLvXdCWCheW3HcpMpcNa", salt, atr, acc1, 20000L, 0l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_034_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_035_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = Base64.getDecoder().decode("WtfKv7fMmgoowbOuJHKb4Q==");
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnoraml_036_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = Base64.getDecoder().decode("");
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456",salt , atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58501".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_noraml_037_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[1];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_noraml_038_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_noraml_039_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[1];
			atr[0] = new Attribute("zCBkHt+u2iuyt@#$%^fHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_abnoraml_040_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[1];
			atr[0] = new Attribute("zCBkHt+u2iu#$^$^ZfHfm+w==".getBytes(),"zCBkHt+u2iu$#^*ZfHfm+w==".getBytes(),"zCBkHt+#^%^@tAXZfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_noraml_041_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[1];
			atr[0] = new Attribute("".getBytes(),"".getBytes(),"".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 0l);
			System.out.println(sr);
			assertEquals(true, true);
		} 

		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	
	@Test
	public void test_normal_042_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_043_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, null, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_noraml_044_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 40000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnoraml_045_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 0, 10l);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnoraml_046_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, -20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	@Test
	public void test_abnoraml_047_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			byte[] salt = acc.getSalt();
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			String ontid = "did:ont:"+acc.address;
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_noraml_048_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 10000000000L, 0);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_049_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnoraml_050_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, -10l);
			System.out.println(sr);
			
		} 
		catch(SDKException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("58005".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnoraml_051_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			com.github.ontio.sdk.wallet.Account acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			String addr1 = acc.address;
			byte[] salt = acc.getSalt();
			Account acc1 = OntTest.sdk().getWalletMgr().getAccount(addr1, "123456");
			String ontid = "did:ont:"+acc.address;
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10l);
			System.out.println(sr);
			
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("error").toString();
			if("43001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	
	@Test
	public void test_noraml_052_sendAddAttributes() throws Exception {
		OntTest.logger().description("----------sendAddAttributes----------");
		
		try {
			Account acc1 = OntTest.common().getAccount(0);
			byte[] salt = OntTest.sdk().getWalletMgr().getDefaultAccount().getSalt();
			String ontid = "did:ont:"+acc1.getAddressU160().toBase58();
			
			Attribute[] atr = new Attribute[3];
			atr[0] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[1] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());
			atr[2] = new Attribute("zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes(),"zCBkHt+u2iuytAXZfHfm+w==".getBytes());

			String sr = OntTest.sdk().nativevm().ontId().sendAddAttributes(ontid, "123456", salt, atr, acc1, 20000L, 10000000000l);
			System.out.println(sr);
			assertEquals(true, true);
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	
	@Test
	public void test_base_053_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			Identity ci = OntTest.sdk().getWalletMgr().createIdentity("123456");

			Thread.sleep(5000);
			System.out.println(ci);
			String ontid1 = ci.ontid;		
			System.out.println(ontid1);
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO(ontid1);
			
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_054_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("did:ont:AMdVo#$#%$#45vmmLh5RfFNRrMDMZEQMmzGm");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_055_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("did:ont:AWHDFD4reQsd7pweSk3J8NLjXJHo6onAZiabc");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_056_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("did:ont:AWHDFD4reQsd7peSk3J8NLjXJHo6onAZiabc");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_057_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("did:ont:AWHDFD4reQsd7pweS@#$%NLjXJHo6onAZiabc");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_058_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("did:AWHDFD4reQsd7pweSk3J8NLjXJHo6onAZiabc");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_059_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("ont:AWHDFD4reQsd7pweSk3J8NLjXJHo6onAZiabc");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
				assertEquals(true, true);
			}
		} 
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_060_sendGetDDO() throws Exception {
		OntTest.logger().description("----------sendGetDDO----------");
		
		try {
			
			String sd = OntTest.sdk().nativevm().ontId().sendGetDDO("");
			System.out.println(sd);
			if(sd.equals("")) {
				System.out.println("ontid为空");
			}
		} 
		catch(RpcException e) {
			Map er = (Map)JSON.parse(e.getMessage());
			OntTest.logger().error(er.toString());
			String er_code = er.get("Error").toString();
			if("47001".equals(er_code)) {
				assertEquals(true,true);
			}
			else {
				assertEquals(true,false);
			}
		}
		catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
	

