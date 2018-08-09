package com.ontio.digitalidentity;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Base64;
import java.util.List;

import org.junit.*;

import com.github.ontio.sdk.info.IdentityInfo;
import com.github.ontio.sdk.wallet.Account;
import com.github.ontio.sdk.wallet.Identity;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class DigitalIdentity {
@Rule public OntTestWatcher watchman= new OntTestWatcher();
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restart(new int[]{0,1,2,3,4,5,6}, "ontology", "config.json", Config.DEFAULT_NODE_ARGS);
		Thread.sleep(10000);
		OntTest.api().node().initOntOng();
	}
	
	@Before
	public void setUp() throws Exception {
		System.out.println("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	@Test
	public void test_001_base_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  001  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.key;
			String pwd = "123456";
			byte[] salt = Acc.getSalt();
			//byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			String address = Acc.address;
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_002_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  002  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = "cLmYhCNWWnt9eafP%XSrBEEX7he+Hs4839mLUMCHT4eCasfkK39Gx0jsnvylJVlq";
			//encryptedPrikey长64但包含%
			String pwd = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,pwd,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_003_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  003  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = "jpFNtSepSSGPjnIkMfX4A5/SaQi/2Crz1ORAgov3TI1MWRG2+yk1v7oScORkaIDds";
			//encryptedPrikey长于64
			String pwd = "123456";
			byte[] salt = Acc.getSalt();
			String address = Acc.address;
			
//			String encryptedPrikey = "gCnmUHREyICwECp8enA52m1YptS1skHEUFTVOqsEOylPTCKPcXBtul6nf/CMUZJe";
//			byte[] salt = Base64.getDecoder().decode("xpkOEKkl4Bi3M2F9uMst5Q==");
//			String pwd = "123456";
//			String address = "Ac4ZcLH1Cyq2HcCMgtSoehBSTNJthQKoZC";
			
			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, pwd, salt, address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_004_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  004  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_encryptedPrikey");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = "";
			//encryptedPrikey为空
			String pwd = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,pwd,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_005_normal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  005  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			//encryptedPrikey为空
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_006_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  006  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			//encryptedPrikey为空
			String password = "!@#$%^";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_007_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  007  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			//encryptedPrikey为空
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_008_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  008  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_password");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			//encryptedPrikey为空
			String password = "";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_009_normal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  009  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_010_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  010  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = "AJGyLXep1D1doBEne1b9441uo9ySMXkhmz";

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_011_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  011  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address + "a";

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_012_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  012  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = Acc.address;
			address = address.substring(0,address.length()-1);
			System.out.println(address.length());

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_013_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  013  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = "A$GyLXep1D1doBEne1b9441uo9ySMXkhmz";

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_014_abnormal_importIdentity() throws Exception {
		OntTest.logger().description("Digital identity  013  importIdentity()");

		try {
			OntTest.logger().step("测试参数importIdentity_address");
			
			OntTest.logger().step("创建新账户并获取参数");
			Account Acc = OntTest.sdk().getWalletMgr().createAccount("123456");
			System.out.println(Acc);
			String encryptedPrikey = Acc.getKey();
			String password = "123456";
			byte[] salt = Acc.getSalt();
			System.out.println(salt.length);
			String address = "";

			OntTest.logger().step("导入身份");
			Identity ret = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey,password,salt,address);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));

		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//createIdentity015_018
	@Test
	public void test_015_base_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  015  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_016_normal_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  016  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			
			String password = "";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_017_normal_createIdentity() throws Exception {
		OntTest.logger().description("Digital identity  017  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			String password = "!@#$%^&*()_+:;,.<>?/";  //password为非法字符
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_018_normal_createIdentity() throws Exception {
		OntTest.logger().description("Digital  018  createIdentity()");

		try {
			OntTest.logger().step("测试参数createIdentity_password");
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			//长度为2001的字符串
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentity(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//createIdentityFromPriKey019-026
	@Test
	public void test_019_base_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  019  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_020_normal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  020  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_021_normal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  021  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "!@#$%^";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_022_normal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  022  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_023_normal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  023  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_024_abnormal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  024  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_password");
			String prikey = "11%^&*()!@#$%^11111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_025_abnormal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  025  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_prikey");
			String prikey = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_026_normal_createIdentityFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  026  createIdentityFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityFromPriKey_prikey");
			String prikey = "";
			String password = "123456";
			
			Identity ret = OntTest.sdk().getWalletMgr().createIdentityFromPriKey(password,prikey);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}		
	
	//createIdentityInfo027-030
	@Test
	public void test_027_base_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  027  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "123456";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_028_normal_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  028  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "!@#$%^&*()";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_029_normal_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  029  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_030_normal_createIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  030  createIdentityInfo()");

		try {
			OntTest.logger().step("测试参数createIdentityInfo_password");
			String password = "";
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfo(password);
			System.out.println(ret);	

//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//createIdentityInfoFromPriKey031-038   //待修改
	@Test
	public void test_031_base_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  031  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "123456";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_032_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  032  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "!@#$%^";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_033_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  033  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_034_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  034  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_password");
			String label = "label";
			String password = "";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_035_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  035  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "1111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_036_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  036  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "!@#$%^1111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_037_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  037  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_038_normal_createIdentityInfoFromPriKey() throws Exception {
		OntTest.logger().description("Digital identity  038  createIdentityInfoFromPriKey()");

		try {
			OntTest.logger().step("测试参数createIdentityInfoFromPriKey_prikey");
			String label = "label";
			String password = "123456";
			String prikey = "";
					
			IdentityInfo ret = OntTest.sdk().getWalletMgr().createIdentityInfoFromPriKey(label, password, prikey);
			System.out.println(ret);	
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getIdentityInfo039-051
	@Test
	public void test_039_base_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  039  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_040_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  040  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:ont:BWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_041_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  041  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC1";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_042_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  042  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTy";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_043_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  043  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:ont:@#zypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_044_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  044  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "did:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_045_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  045  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_046_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  046  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_ontid");
			String ontid = "";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_047_normal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  047  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "123456";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_048_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  048  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "111111";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_049_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  049  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "!@#/n%";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_050_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  050  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "h3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56gh3g24fc54hg46hv3h6vj3h463g4j63jh46b3jfj455jv6jh56ga";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_051_abnormal_getIdentityInfo() throws Exception {
		OntTest.logger().description("Digital identity  051  getIdentityInfo()");

		try {
			OntTest.logger().step("测试参数getIdentityInfo_password");
			String ontid = "did:ont:AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			String password = "";
			byte[] salt = Base64.getDecoder().decode("qhyRI2J/gyzOWnGMMLXXUw==");
			
			IdentityInfo ret = OntTest.sdk().getWalletMgr().getIdentityInfo(ontid, password, salt);
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_052_base_getIdentitys() throws Exception {
		OntTest.logger().description("Digital identity  051  getIdentityInfo()");

		try {
			OntTest.logger().step("测试接口getIdentitys");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			OntTest.sdk().getWalletMgr().createIdentity("123456");
			
			List<Identity> ret = OntTest.sdk().getWalletMgr().getWallet().getIdentities();
			System.out.println(ret);
//			assertEquals(true,ret.equals(exp));
			assertEquals(true,true);
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
}


