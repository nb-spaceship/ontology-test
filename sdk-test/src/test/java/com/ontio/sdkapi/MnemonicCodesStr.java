package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.util.Base64;
import java.util.Map;

import javax.xml.bind.DatatypeConverter;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;

import com.github.ontio.common.WalletQR;
import com.github.ontio.core.block.Block;
import com.github.ontio.crypto.MnemonicCode;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.sdk.wallet.Account;
import com.github.ontio.sdk.wallet.Identity;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class MnemonicCodesStr {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
//		OntTest.api().node().restartAll("ontology", "config.json", Config.DEFAULT_NODE_ARGS);
//		Thread.sleep(5000);
	}
	
	@Before
	public void setUp() throws Exception {
		System.out.println("setUp");
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	//generateMnemonicCodesStr001-006
	@Test
	public void test_base_001_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  001  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_walletFile");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			System.out.println(walletFile);
			System.out.println(identity);
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_002_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  002  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode");
			
			String encryptedPrikey = "ShZUA3U4vPQHnzIKX1FSiICzMsoYPBJ5+H13OR2dZx/hhmhIA5e8eLEFnJinFn9B";
			String password = "123456";
			String salt0 = "By9R6hmWNB9zLh+gqgSHRw==";
			byte[] salt = Base64.getDecoder().decode(salt0);
			String address = "Af296avwQTqHV5byLvXdCWCheW3HcpMpcN";
			Identity identity = OntTest.sdk().getWalletMgr().importIdentity(encryptedPrikey, password, salt, address);
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
//			String addr = OntTest.common().getAccount(0).getAddressU160().toBase58();
//			String ontid = "did:ont:"+addr;
//			Identity identity = walletFile.getIdentity(ontid);
			
			System.out.println(walletFile);
			System.out.println(identity);
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	//待修改
	@Test
	public void test_abnormal_003_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  003  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_walletFile");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = null;
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_004_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  004  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_identity");
			
			Identity identity = OntTest.sdk().getWalletMgr().createIdentity("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	//待修改
	@Test
	public void test_abnormal_005_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  005  exportIdentityQRCode()");

		try {
			Identity identity = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	//待修改
	@Test
	public void test_abnormal_006_exportIdentityQRCode() throws Exception {
		OntTest.logger().description("助记词  006  exportIdentityQRCode()");

		try {
			OntTest.logger().step("测试参数exportIdentityQRCode_identity");
			
			Identity identity = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportIdentityQRCode(walletFile,identity);   
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//exportAccountQRCode007-012
	@Test
	public void test_base_007_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  007  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_walletFile");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_abnormal_008_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  008  exportAccountQRCode()");

		try {
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = null;
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_abnormal_009_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  009  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_walletFile");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = null;
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_010_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  010  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_account");
			
			Account account = OntTest.sdk().getWalletMgr().createAccount("123456");
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_011_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  011  exportAccountQRCode()");

		try {
			Account account = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_012_exportAccountQRCode() throws Exception {
		OntTest.logger().description("助记词  012  exportAccountQRCode()");

		try {
			OntTest.logger().step("测试参数exportAccountQRCode_account");
			
			Account account = null;
			Wallet walletFile = OntTest.sdk().getWalletMgr().getWallet();
			
			Map QRcode = WalletQR.exportAccountQRCode(walletFile, account);
			System.out.println(QRcode);
//			assertEquals(true,ret.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getPriKeyFromQrCode013-019  待修改 待添加
	@Test
	public void test_base_013_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  013  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_014_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  014  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_015_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  015  getPriKeyFromQrCode()");

		try {
			String qrcode = "";
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_016_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  016  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "123456";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_017_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  017  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "111111";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_018_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  018  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "@#$%%";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_019_getPriKeyFromQrCode() throws Exception {
		OntTest.logger().description("助记词  019  getPriKeyFromQrCode()");

		try {
			String qrcode = "qrcode";
			String password = "";
			String PriKey = WalletQR.getPriKeyFromQrCode(qrcode, password);
			
			System.out.println(PriKey);
			assertEquals(true,true);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//generateMnemonicCodesStr020
	@Test
	public void test_base_020_generateMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  020  generateMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数generateMnemonicCodesStr");
			
			String codesStr = MnemonicCode.generateMnemonicCodesStr();
			System.out.println(codesStr);
//			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//getSeedFromMnemonicCodesStr021-025
	@Test
	public void test_base_021_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  021  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "F7BB3B035211AF5C8A4CB4B78975A3EB91768CCAFD1DA4EECCC72D993D98DDA40409727FF7EAE1DE20347844F90873863207E8241BB4895BC150B54FD0315D7C";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_022_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  022  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "!@#$$% smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			//包含非法字符
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "BC6FD5093DA6AC09857D4DA0B33E34C3C5E72B4E49521A80321EB81EFAAA6828E46B080BAA32F9F779F81FB05B6CF13468FBA5F9D836011F7232ADF807DC6E32";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}		
	
	@Test
	public void test_normal_023_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  023  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth mine craft";
			//多余一个助记词
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "DECFBA55E8DC3A3E4724241340EDB778AF760FB0FF94C8C10525DBADB541D989B30EF97FBC269EB05ACB01B77B1C894BE7B3FC84B15F5BBE3BD392FFCE99AE23";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_024_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  024  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			//缺少一个助记词
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "3B63D84257B005769F0495D5B80102BC3CB6BC1F002890BB8AA43D7A595B9B8DC84293836D40A0D497DC8E4139D78647776E1EB24B5BDCBC2C1B47EC55B1BC96";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_025_getSeedFromMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  025  getSeedFromMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数getSeedFromMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "";
			//助记词不存在
			
			byte[] byte_seed = MnemonicCode.getSeedFromMnemonicCodesStr(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "4ED8D4B17698DDEAA1F1559F152F87B5D472F725CA86D341BD0276F1B61197E21DD5A391F9F5ED7340FF4D4513AAB9CCE44F9497A5E7ED85FD818876B6EB402E";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	//getPrikeyFromMnemonicCodesStrBip44 026-030
	@Test
	public void test_normal_026_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  026  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "8B5DCA591BFC0A455CE6A6A9225C57F09284BED6535C1E25ACA898CFFEB11EAB";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_027_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  027  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "!@#$ smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "B7AC16D5A348BD6189972052D4742FD75A51767C20D07ED4A0F27161A11019F4";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_028_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  028  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "mine polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_Prikey = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_Prikey.length);
			String ret = DatatypeConverter.printHexBinary(byte_Prikey);
			System.out.println(ret);
			
			String exp = "FC5871DD267A5A5A7416DEEB4CD102B623C5DD963E04E3ED1161C4B6A835510B";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_029_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  029  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			
			byte[] byte_seed = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_seed.length);
			String ret = DatatypeConverter.printHexBinary(byte_seed);
			System.out.println(ret);
			
			String exp = "1DB4A2B491B92159C3DBAF76A3EF23DCCA86E408002C7506ACC2A74013825A62";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_030_getPrikeyFromMnemonicCodesStrBip44() throws Exception {
		OntTest.logger().description("助记词  030  getPrikeyFromMnemonicCodesStrBip44()");

		try {
			OntTest.logger().step("测试参数getPrikeyFromMnemonicCodesStrBip44_mnemonicCodesStr");
			String mnemonicCodesStr = "";
			
			byte[] byte_Prikey = MnemonicCode.getPrikeyFromMnemonicCodesStrBip44(mnemonicCodesStr);
			System.out.println(byte_Prikey.length);
			String ret = DatatypeConverter.printHexBinary(byte_Prikey);
			System.out.println(ret);
			
			String exp = "FC7C42A4C1017ACAFF4B5FB1A18CF132948ECC70DF6394F780887D1F281E487A";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//encryptMnemonicCodesStr 031-044
	@Test
	public void test_base_031_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  031  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_032_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  032  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "@#%$ smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "Q1Xmv9P8+J6TIGJfg+iaR8QxI8XR6+UinGP6D+ilDlrV92aOdF49tWuQjiEAPpfE4u2N75YQCkXyl/8N2kH2f6YhYTWnBVJGL/wdWX4J";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_033_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  033  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "mine polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "bh+t/tP/+p2dJioMneaZR4x9NcfJ6rcr2XT8FeqoVw7Q6nmIal4kpnaMhnZOPI3f6PyN/J8NG0agib4Uz03qMfQpdC6sRFQDKOMXV35BIcKasaAR";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_034_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  034  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "cBus9IfntYKdOH5fnOyVR5EvI4bR7Pg31G6oF+qiGR2C62iSYREk9HqKiDNGfY/M8//I7ZlEE0Hpl/8S3lzqOrUwNTSvC0kSNA==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_035_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  035  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_mnemonicCodesStr");
			String mnemonicCodesStr = "";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_036_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  036  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_037_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  037  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "000000";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "XKqTakzgL2X1hi6lqeDNV5gc/9hUiJYRwFPsbeVizhQ+3kfrZVK7dUx8VPXVXOi7bLj+IcpfsfsDwj408I42wws79kkbV4qq/HizZAb6xw==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_038_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  038  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "@#￥%&";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "kLvFG1oAEGuvEzs9HSDfbhFFgfxNsODJqkMCnq2A9PYrftJ95aymuK9VCWqOx3/RGTel/Umrm6ysc8zKqkWaAJB9taBgZvjV+hYjAOTnZQ==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_039_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  039  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "bUPnO9pR+nxTL50ycHovFi88CFovnnaq8xREaaaax3T1DH/FXc4R56LsBr9kcWi6qT4gEJI+GIk8U1CkKIPqnzpNWXdu6OfR5KQr0JF7+A==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_040_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  040  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_041_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  041  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "ABCypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "e/E3Gw01JyXT1DGmDk1/wmcNSSlT4D/tKsvMMhVciULa7wqqm5v8ziFqImyoEkZh8DB72bi45hFs6jkNIL0wRk3w2d8nHKKbB1/p0qhVHw==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_042_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  042  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC1";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "P1U+mYLoLSX125W8TsijowOcPhxLMZr4w9R8tGaucI0UDrLIZ5MaPv6KDA9tI9VCOc+96fc/z30c9ToRsGKlx/0xtQGHcYmT2xqsJ7wcHA==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_043_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  043  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "@#$ypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "3oJzbPSMZz4cjEqbL9FNlKQT8TfuAHFRC3cQ3jA5Hytej8I3upGAHdWynUc/ltw2fH56K2UzBHhj86kI/X/bn4YEvShwmOGQjvV1ObY4Ow==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_044_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  044  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String password = "123456";
			String address = "";
			
			String ret = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println(ret);
			
			String exp = "oKP998ISTB/Xc91YBSq5iAAOsR4NOWfrH8JIamgWFg8yi0gVyDNh9YvKdvlu44Xy8nmpZh3H8Qv6FCffQRVpEUJLstnAbYwSi39RidzV3w==";	
			assertEquals(true,ret.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	//decryptMnemonicCodesStr045-058 待修改 待添加
	@Test
	public void test_base_045_decryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  045  decryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String mnemonicCodesStr = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String encryptStr = MnemonicCode.encryptMnemonicCodesStr(mnemonicCodesStr, password, address);
			System.out.println("encryptStr = "+encryptStr);
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	

	@Test
	public void test_abnormal_046_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  046  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String encryptedStr = "KVeDuNev5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "*!@#$ smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_047_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  047  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String encryptedStr = "bBi38pyv5Z6QNXhfg+SZXJA1ZtXE8uNn0HLrFO2/ElrW92aQewdzo2uNjzEAM57f9eTav5QMF0Xm2a8Bz1z9LbpkeCarCgYUOeUAU2sVctyYsbsN4Q==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "ontio polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_048_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  048  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String encryptedStr = "cBus9IfntYKdOH5fnOyVR5EvI4bR7Pg31G6oF+qiGR2C62iSYREk9HqKiDNGfY/M8//I7ZlEE0Hpl/8S3lzqOrUwNTSvC0kSNA==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_abnormal_049_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  049  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_encryptedMnemonicCodesStr");
			
			String encryptedStr = "";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_050_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  050  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_051_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  051  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "111111";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_052_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  052  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "@#$%%^";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_053_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  053  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_password");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_054_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  054  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(true,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_055_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  055  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "BWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}

	@Test
	public void test_abnormal_056_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  056  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "1AWzypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_057_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  057  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "@#zypEQCfN5iCyqawNMKRnnk3BctA4RTyC";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_abnormal_058_encryptMnemonicCodesStr() throws Exception {
		OntTest.logger().description("助记词  058  encryptMnemonicCodesStr()");

		try {
			OntTest.logger().step("测试参数encryptMnemonicCodesStr_address");
			
			String encryptedStr = "cxmv+oGv5pyTO34X0PqXX5B9KsPG6uI12Tf8Eve9HwOC8nuPfRlzuniQkzlXfZzF7u7Lv4cFClTli7FA1knxMfQ2cDOwAUcSfOIfWWUVOg==";
			String password = "123456";
			String address = "";
			
			String decryptStr = MnemonicCode.decryptMnemonicCodesStr(encryptedStr, password, address);
			
			System.out.println(decryptStr);
			String exp = "polar smooth salt lecture trophy wrong narrow chief pattern main retreat smooth";	
			assertEquals(false,decryptStr.equals(exp));
			
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
}
