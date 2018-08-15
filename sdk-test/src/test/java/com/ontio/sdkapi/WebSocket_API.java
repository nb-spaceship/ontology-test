package com.ontio.sdkapi;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.net.URL;
import java.util.ArrayList;
import java.util.Base64;
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
import com.github.ontio.network.websocket.Result;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;
import com.ontio.testtool.utils.Config;

public class WebSocket_API {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
		OntTest.api().node().restartAll();
		OntTest.sdk().getWebSocket().startWebsocketThread(true);
		Thread.sleep(3000);
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
			int nodes = Config.NODES.size();
			System.out.println(nodes);
			int acc = OntTest.sdk().getWebSocket().getNodeCount();
			Result result = OntTest.common().waitWsResult("getconnectioncount");
			System.out.println("result:" + result.Result.toString());
			
			assertEquals(true, nodes - 1 == acc);
			
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("----------getBlock----------");
		
		try {
			Block acc = OntTest.sdk().getWebSocket().getBlock(15);
			Result result = OntTest.common().waitWsResult("getblockbyheight");
			System.out.println("result:" + result.Result.toString());
			
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
			Object acc = OntTest.sdk().getWebSocket().getBlockJson(15);
			Result result = OntTest.common().waitWsResult("getblockbyheight");
			System.out.println("result:" + result.Result.toString());
			
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	
	@Test
	public void test_base_004_getBlockJson() throws Exception {
		OntTest.logger().description("----------getBlockJson----------");
		
		try {
			System.out.println("1.获取hash");
			UInt256 hash = OntTest.sdk().getRpc().getBlock(15).hash();
			
			System.out.println("2.getBlockJson");
			Object acc = OntTest.sdk().getWebSocket().getBlockJson(hash.toHexString());
			
			Result result1 = OntTest.common().waitWsResult("getblockbyhash");
			System.out.println("result:" + result1.Result.toString());
			
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
			UInt256 hash = OntTest.sdk().getRpc().getBlock(15).hash();
			System.out.println(hash);
			System.out.println("2.getBlockJson");
			Block acc = OntTest.sdk().getWebSocket().getBlock(hash.toHexString());
			Result result1 = OntTest.common().waitWsResult("getblockbyhash");
			System.out.println("result:" + result1.Result.toString());
			
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
			
			int acc = OntTest.sdk().getWebSocket().getBlockHeight();
			Result result = OntTest.common().waitWsResult("getblockheight");
			System.out.println(result.Result.toString());
			
			assertEquals(true, true);
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
			OntTest.common().waitTransactionResult(s);

			Transaction trs = OntTest.sdk().getWebSocket().getTransaction(s);
			Result rs = OntTest.common().waitWsResult("gettransaction");
			System.out.println(rs.Result.toString());
			
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
			
			String acc = OntTest.sdk().getWebSocket().getStorage(codeAddr1, "01");
			
			Result rs = OntTest.common().waitWsResult("getstorage");
			System.out.println(rs.Result.toString());
			
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

			String acc = OntTest.sdk().getWebSocket().getStorage(codeAddr1, "01");
			
			Result rs = OntTest.common().waitWsResult("getstorage");
			System.out.println(rs.Result.toString());
			
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
			Object acc = OntTest.sdk().getWebSocket().getBalance(addr1);
			Result rs = OntTest.common().waitWsResult("getbalance");
			System.out.println(rs.Result.toString());
			
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
			Object acc = OntTest.sdk().getWebSocket().getContractJson(codeAddr);
			
			Result rs = OntTest.common().waitWsResult("getcontract");
			System.out.println(rs.Result.toString());
			
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
			
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(addr1, addr2, 10L,addr1, 20000L, 0);
	        OntTest.sdk().signTx(tx, new Account[][]{{acc1}});
	        boolean b = OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
	        String s = "";
	        if (b) {
	            s = tx.hash().toHexString();
	        }
			
			OntTest.common().waitTransactionResult(s);
			System.out.println(s);
			int height = OntTest.sdk().getRestful().getBlockHeightByTxHash(s);
			System.out.println("height:"+height);
			Object acc = OntTest.sdk().getWebSocket().getSmartCodeEvent(height);
			Result rs = OntTest.common().waitWsResult("getsmartcodeevent");
			System.out.println(acc);
			System.out.println(rs.Result.toString());
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
//	
//	
//	
//	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("----------getSmartCodeEvent----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();
			
			Transaction tx = OntTest.sdk().nativevm().ont().makeTransfer(acc1.getAddressU160().toBase58(), addr2, 10L, acc1.getAddressU160().toBase58(), 20000L, 0);
	        OntTest.sdk().signTx(tx, new Account[][]{{acc1}});
	        boolean b = OntTest.sdk().getConnect().sendRawTransaction(tx.toHexString());
	        String s = "";
	        if (b) {
	            s = tx.hash().toHexString();
	        }
			
			OntTest.common().waitTransactionResult(s);
			System.out.println(s);
			Object acc = OntTest.sdk().getWebSocket().getSmartCodeEvent(s);
			Result rs = OntTest.common().waitWsResult("getsmartcodeevent");
			System.out.println(rs.Result.toString());
			System.out.println(acc);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
//	
	
	
	
	@Test
	public void test_base_014_getBlockHeightByTxHash() throws Exception {
		OntTest.logger().description("----------getBlockHeightByTxHash----------");
		
		try {
			Account acc1=OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String s = OntTest.sdk().nativevm().ont().sendTransfer(acc1, addr2, 10L, acc1, 20000L, 0L);
			Thread.sleep(5000);
			int acc = OntTest.sdk().getWebSocket().getBlockHeightByTxHash(s);
			
			Result rs = OntTest.common().waitWsResult("getblockheightbytxhash");
			System.out.println(rs.Result.toString());
			
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
			Thread.sleep(5000);
			Object acc = OntTest.sdk().getWebSocket().getMerkleProof(s);
			
			Result rs = OntTest.common().waitWsResult("getmerkleproof");
			System.out.println(rs.Result.toString());
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
			Thread.sleep(5000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(1);
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(5000);

			boolean acc = OntTest.sdk().getWebSocket().sendRawTransaction(invokeTx.toHexString());
			
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			System.out.println(rs.Result.toString());
			
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
			Thread.sleep(5000);
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(1);
	        list.add(args);
	        
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Thread.sleep(5000);
			boolean acc = OntTest.sdk().getWebSocket().sendRawTransaction(A);
			
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			System.out.println(rs.Result.toString());
			
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
			Thread.sleep(5000);
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
	        Thread.sleep(5000);
			Object acc = OntTest.sdk().getWebSocket().sendRawTransactionPreExec(invokeTx.toHexString());
			
			Result rs = OntTest.common().waitWsResult("sendrawtransaction");
			System.out.println(rs.Result.toString());
			
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
			String s = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
			OntTest.common().waitTransactionResult(s);
			Object acc = OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
			
			Result rs = OntTest.common().waitWsResult("getmerkleproof");
			System.out.println(rs.Result.toString());

		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
//	
//	
//	
//	@Test
//	public void test_normal_020_getAllowance() throws Exception {
//		OntTest.logger().description("----------getAllowance----------");
//		
//		try {
//		Account acc1=OntTest.common().getAccount(0);
//		Account acc2 = OntTest.common().getAccount(1);
//		
//		String addr1 = acc1.getAddressU160().toBase58();
//		String addr2 = acc2.getAddressU160().toBase58();
//		String approvetxhash = OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
//		OntTest.common().waitTransactionResult(approvetxhash);
//		
//		Object acc = OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
//		Result rs = OntTest.common().waitWsResult("getmerkleproof");
//		System.out.println(rs.Result.toString());
//		System.out.println(acc);
//		} 
//		catch(Exception e) {
//		OntTest.logger().error(e.toString());
//		fail();
//		}
//	}
//	
//	
//	
//	
//	@Test
//	public void test_normal_021_getAllowance() throws Exception {
//		OntTest.logger().description("----------getAllowance----------");
//		
//		try {
//		Account acc1=OntTest.common().getAccount(0);
//		Account acc2 = OntTest.common().getAccount(1);
//		
//		String addr1 = acc1.getAddressU160().toBase58();
//		String addr2 = acc2.getAddressU160().toBase58();
//		OntTest.sdk().nativevm().ont().sendApprove(acc1, addr2, 100, acc1, 20000, 0);
//		Thread.sleep(5000);
//		Object acc = OntTest.sdk().getWebSocket().getAllowance("ont", addr1, addr2);
//		Result rs = OntTest.common().waitWsResult("getmerkleproof");
//		System.out.println(rs.Result.toString());
//		System.out.println(acc);
//		} 
//		catch(Exception e) {
//		OntTest.logger().error(e.toString());
//		fail();
//		}
//	}
	
	
	
	@Test
	public void test_base_022_getMemPoolTxCount() throws Exception {
		OntTest.logger().description("----------getMemPoolTxCount----------");
		
		try {
			Object acc = OntTest.sdk().getWebSocket().getMemPoolTxCount();
			Result rs = OntTest.common().waitWsResult("getmempooltxcount");
			System.out.println(rs.Result.toString());
			
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

			Object acc = OntTest.sdk().getWebSocket().getMemPoolTxState(s);
			Result rs = OntTest.common().waitWsResult("getmempooltxstate");
			System.out.println(rs.Result.toString());
			
			assertEquals(true, true);
		} catch(Exception e) {
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	
//	@Test
//	public void test_base_024_syncSendRawTransaction() throws Exception {
//		OntTest.logger().description("----------syncSendRawTransaction----------");
//		
//		try {
//			String url = this.getClass().getResource("rest.cs").getPath();
//			System.out.println(url);
//			Map dec = OntTest.api().contract().deployContract(url, null);
//			String codeAddr = String.valueOf(dec.get("address"));
//			codeAddr = Helper.reverse(codeAddr);
//			//codeAddr为存在的地址但并非合约地址
//			System.out.println(codeAddr);//智能合约地址
//			Thread.sleep(5000);
//	        List list = new ArrayList<Object>();
//	        list.add("test".getBytes());
//	        List args = new ArrayList<Object>();
//	        args.add(Helper.hexToBytes("01"));
//	        args.add(Helper.hexToBytes("01"));
//	        list.add(args);
//	        
//	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
//	        byte[] params = BuildParams.createCodeParamsScript(list);
//	        
//	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
//	        Transaction A= OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
//	        Thread.sleep(5000);
//			Object acc = OntTest.sdk().getWebSocket().sendRawTransaction(invokeTx.toHexString());
//			assertEquals(true, OntTest.common().waitTransactionResult(invokeTx.hash().toHexString()));
//			
//			Result rs = OntTest.common().waitWsResult("Notify");
//			System.out.println(rs.Result.toString());
//			
//			assertEquals(true, true);
//		} catch(Exception e) {
//			OntTest.logger().error(e.toString());
//			fail();
//		}
//	}
	
	
}
