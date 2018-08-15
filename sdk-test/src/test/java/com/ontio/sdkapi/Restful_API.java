package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.net.URL;
import java.security.Key;
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
import com.github.ontio.common.UInt256;
import com.github.ontio.core.block.Block;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class Restful_API {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
//		OntTest.api().node().restartAll("ontology", "test_config.json", Config.DEFAULT_NODE_ARGS);
//		Thread.sleep(8000);
	}
	
	@Before
	public void setUp() throws Exception {
		
	}
	
	@After
	public void TearDown() throws Exception {
		System.out.println("TearDown");
	}
	
	@Test
	public void test_base_001_getNodeCount() throws Exception {
		OntTest.logger().description("----------getNodeCount----------");
		
		try {
			int acc = OntTest.sdk().getRestful().getNodeCount();
			System.out.println(acc);
			assertEquals(true, acc > 0);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			Block acc = OntTest.sdk().getRestful().getBlock(15);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_003_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			Object acc = OntTest.sdk().getRestful().getBlockJson(15);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_004_getBlock() throws Exception {
		OntTest.logger().description("----------getNodeCount----------");
		
		try {
			System.out.println("1.获取hash");
			UInt256 hash = OntTest.sdk().getRestful().getBlock(15).hash();
			System.out.println(hash);
			System.out.println("2.getBlockJson");
			Object acc = OntTest.sdk().getRestful().getBlockJson(hash.toHexString());
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_005_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			System.out.println("1.获取hash");
			UInt256 hash = OntTest.sdk().getRestful().getBlock(15).hash();
			System.out.println(hash);
			System.out.println("2.getBlockJson");
			Block acc = OntTest.sdk().getRestful().getBlock(hash.toHexString());
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_006_getBlockHeight() throws Exception {
		OntTest.logger().description("----------getBlockHeight----------");
		
		try {
			int acc = OntTest.sdk().getRestful().getBlockHeight();
			System.out.println(acc);
			assertEquals(true, acc > 0);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_007_getTransaction() throws Exception {
		OntTest.logger().description("----------getTransaction----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(8000);
			Transaction trs = OntTest.sdk().getRestful().getTransaction(s);
			System.out.println(trs.toHexString());
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_008_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("06"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			String acc = OntTest.sdk().getRestful().getStorage(codeAddr1, "01");
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_normal_009_getStorage() throws Exception {
		OntTest.logger().description("----------getStorage----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr1 = String.valueOf(dec.get("address"));
			String codeAddr2 = Helper.reverse(codeAddr1);
			
			List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("06"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr2, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1"+b1);

			OntTest.sdk().getConnect().sendRawTransaction(invokeTx.toHexString());
			OntTest.common().waitTransactionResult(invokeTx.hash().toHexString());
			String acc = OntTest.sdk().getRestful().getStorage(codeAddr1, "01");
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_010_getBalance() throws Exception {
		OntTest.logger().description("----------getBalance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			
			String addr1 = acc1.getAddressU160().toBase58();
			Object acc = OntTest.sdk().getRestful().getBalance(addr1);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_011_getContractJson() throws Exception {
		OntTest.logger().description("----------getContractJson----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));

			Object acc = OntTest.sdk().getRestful().getContractJson(codeAddr);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_012_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			OntTest.common().waitTransactionResult(s);
			int height = OntTest.sdk().getRestful().getBlockHeightByTxHash(s);
			System.out.println("height:"+height);
			Object acc = OntTest.sdk().getRestful().getSmartCodeEvent(height);
			System.out.println(acc);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			
			Thread.sleep(7000);
			Object acc = OntTest.sdk().getRestful().getSmartCodeEvent(s);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	
	@Test
	public void test_base_014_getBlockHeightByTxHash() throws Exception {
		OntTest.logger().description("----------getBlockHeightByTxHash----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(8000);
			int acc = OntTest.sdk().getRestful().getBlockHeightByTxHash(s);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_015_getMerkleProof() throws Exception {
		OntTest.logger().description("----------getMerkleProof----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().getMerkleProof(s);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_016_sendRawTransaction() throws Exception {
		OntTest.logger().description("----------sendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			System.out.println(codeAddr);//智能合约地址
			Thread.sleep(8000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(8000);

			boolean acc = OntTest.sdk().getRestful().sendRawTransaction(invokeTx.toHexString());
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_base_017_sendRawTransaction() throws Exception {
		OntTest.logger().description("----------sendRawTransaction----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			System.out.println(codeAddr);//智能合约地址
			Thread.sleep(8000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(8000);
			boolean acc = OntTest.sdk().getRestful().sendRawTransaction(A);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_018_sendRawTransactionPreExec() throws Exception {
		OntTest.logger().description("----------sendRawTransactionPreExec----------");
		
		try {
			String url = this.getClass().getResource("rest.cs").getPath();
			Map dec = OntTest.api().contract().deployContract(url, null);
			String codeAddr = String.valueOf(dec.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			System.out.println(codeAddr);//智能合约地址
			Thread.sleep(8000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
//	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().sendRawTransactionPreExec(invokeTx.toHexString());
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_019_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	
	@Test
	public void test_normal_020_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			System.out.println(acc);
			assertEquals(true, true);
		} 
		catch(Exception e) {
		OntTest.logger().error(e.toString());
		fail();
		}
	}
	
	
	
	
	@Test
	public void test_normal_021_getAllowance() throws Exception {
		OntTest.logger().description("----------getAllowance----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().getAllowance("ont", addr1, addr2);
			System.out.println(acc);
			assertEquals(true, true);
		} 
		catch(Exception e) {
		OntTest.logger().error(e.toString());
		fail();
		}
	}
	
	
	
	@Test
	public void test_base_022_getMemPoolTxCount() throws Exception {
		OntTest.logger().description("----------getMemPoolTxCount----------");
		
		try {
			Object acc = OntTest.sdk().getRestful().getMemPoolTxCount();
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_023_getMemPoolTxState() throws Exception {
		OntTest.logger().description("----------getMemPoolTxState----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 100, acc1, 20000, 0);
			System.out.println(s);
			Object acc = OntTest.sdk().getRestful().getMemPoolTxState(s);
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	
	@Test
	public void test_base_024_syncSendRawTransaction() throws Exception {
		OntTest.logger().description("----------syncSendRawTransaction----------");
		
		try {
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/neo_ont/ont.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			//codeAddr为存在的地址但并非合约地址
			System.out.println(codeAddr);//智能合约地址
			Thread.sleep(8000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(8000);
			Object acc = OntTest.sdk().getRestful().syncSendRawTransaction(invokeTx.toHexString());
			System.out.println(acc);
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
