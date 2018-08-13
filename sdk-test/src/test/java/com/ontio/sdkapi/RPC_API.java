package com.ontio.sdkapi;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.HashMap;
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
import com.github.ontio.common.WalletQR;
import com.github.ontio.core.block.Block;
import com.github.ontio.core.payload.DeployCode;
import com.github.ontio.core.payload.InvokeCode;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.network.exception.RpcException;
import com.github.ontio.sdk.wallet.Identity;
import com.github.ontio.sdk.wallet.Wallet;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.ontio.OntTestWatcher;
import com.ontio.testtool.OntTest;

public class RPC_API {
	@Rule public OntTestWatcher watchman= new OntTestWatcher();
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		OntTest.init();
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
	public void test_base_001_getNodeCount() throws Exception {
		OntTest.logger().description("RPC_API 001 getNodeCount");

		try {
			OntTest.logger().step("测试getNodeCount()");
			
			int num = OntTest.sdk().getRpc().getNodeCount();
			System.out.println("actual_nodenum = "+num);
			int exp = 16;
			System.out.println("expect_nodenum = "+exp);
			
			assertEquals(true,exp==num);
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_002_getBlock() throws Exception {
		OntTest.logger().description("RPC_API 002 getBlock");

		try {
			OntTest.logger().step("测试getBlock()");
			
			Block Block = OntTest.sdk().getRpc().getBlock(15);
			System.out.println("Block : "+Block);
			int ret = Block.height;
			System.out.println("Block_height = "+ret);
			int exp = 15;
			
			assertEquals(true,ret==exp);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	

	@Test
	public void test_base_003_getBlockJson() throws Exception {
		OntTest.logger().description("RPC_API 003 getBlockJson");

		try {
			OntTest.logger().step("测试getBlock()");
			
			int block_height = 15;
			Object ret_block = OntTest.sdk().getRpc().getBlockJson(block_height);
			System.out.println("ret_blockJson : "+ret_block);
			
			String hash = String.valueOf(OntTest.sdk().getRpc().getBlock(block_height).hash());
			Object exp_block = OntTest.sdk().getRpc().getBlockJson(hash);
			System.out.println("exp_blockJson : "+exp_block);
			
			assertEquals(true,ret_block.equals(exp_block));	
		} catch(RpcException e) {
			int block_height = 15;
			String ret_err = String.valueOf(e);
			System.out.println("The current block was not found ! (block_height = "+block_height+")");
			String exp_err = "com.github.ontio.network.exception.RpcException: {\"result\":\"\",\"id\":1,\"error\":42002,\"jsonrpc\":\"2.0\",\"desc\":\"INVALID PARAMS\"}";
			assertEquals(true,ret_err.equals(exp_err));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_004_getBlockJson() throws Exception {
		OntTest.logger().description("RPC_API 004 getBlockJson");

		try {
			OntTest.logger().step("测试getBlockJson()");
			Block block = OntTest.sdk().getRpc().getBlock(15);
			System.out.println("block : "+block);
			String hash = String.valueOf(block.hash());
			System.out.println("block_hash : "+hash);
			
			Object hash_blockJson = OntTest.sdk().getRpc().getBlockJson(hash);
			System.out.println("ret_blockJson : "+hash_blockJson);
			Object height_blockJson = OntTest.sdk().getRpc().getBlockJson(15);
			System.out.println("exp_blockJson : "+height_blockJson);			
			
			assertEquals(true,hash_blockJson.equals(height_blockJson));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_005_getBlock() throws Exception {
		OntTest.logger().description("RPC_API 005 getBlockJson");

		try {
			OntTest.logger().step("测试getBlock()");
			Block height_block = OntTest.sdk().getRpc().getBlock(15);
			System.out.println("height_block : "+height_block);
			String hash = String.valueOf(height_block.hash());
			System.out.println("block_hash : "+hash);
			
			Block hash_block = OntTest.sdk().getRpc().getBlock(hash);
			System.out.println(hash_block);

			assertEquals(true,hash_block.equals(height_block));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_006_getBlockHeight() throws Exception {
		OntTest.logger().description("RPC_API 006 getBlockHeight");

		try {
			OntTest.logger().step("测试getBlockHeight()");
			
			int h = OntTest.sdk().getRpc().getBlockHeight();
			System.out.println(h);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_007_getTransaction() throws Exception {
		OntTest.logger().description("RPC_API 007 getTransaction");

		try {
			OntTest.logger().step("测试getTransaction()");
			
			
			 
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 1L, acc, 20000L, 0L);
			System.out.println("txhash : "+txhash);
			Thread.sleep(5000);
			//交易哈希
			Transaction Transaction = OntTest.sdk().getRpc().getTransaction(txhash);
			System.out.println("Transaction : "+Transaction);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_base_008_getStorage() throws Exception {
		OntTest.logger().description("RPC_API 008 getStorage");

		try {
			OntTest.logger().step("测试getStorage()");
			
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("11"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1 : "+b1);
	        String hashcode = Integer.toHexString(b1.hashCode());
	        System.out.println("hashcode : "+hashcode);
			
			String key = "";
			String Storage = OntTest.sdk().getRpc().getStorage(hashcode, key);
			System.out.println(Storage);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_normal_009_getStorage() throws Exception {
		OntTest.logger().description("RPC_API 009 getStorage");

		try {
			OntTest.logger().step("测试getStorage()");
			
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("11"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());
	        System.out.println("b1 : "+b1);
	        String hashcode = Integer.toHexString(b1.hashCode());
	        System.out.println("hashcode : "+hashcode);
			
			String key = "";
			String Storage = OntTest.sdk().getRpc().getStorage(hashcode, key);
			System.out.println(Storage);
			
			assertEquals(true,true);		
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	

	@Test
	public void test_base_010_getBalance() throws Exception {
		OntTest.logger().description("RPC_API 010 getBalance");

		try {
			OntTest.logger().step("测试getBalance()");
			String addr = OntTest.common().getAccount(0).getAddressU160().toBase58();
			Object Balance = OntTest.sdk().getRpc().getBalance(addr);
			System.out.println(Balance);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_011_getContractJson() throws Exception {
		OntTest.logger().description("RPC_API 011 getContractJson");

		try {
			OntTest.logger().step("测试getContractJson()");
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
	        
			Object Contract = OntTest.sdk().getRpc().getContractJson(codeAddr);
			System.out.println(Contract);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_012_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("RPC_API 012 getSmartCodeEvent");

		try {
			OntTest.logger().step("测试getSmartCodeEvent()");

			Object SmartCodeEvent = OntTest.sdk().getRpc().getSmartCodeEvent(1);
			System.out.println(SmartCodeEvent);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_013_getSmartCodeEvent() throws Exception {
		OntTest.logger().description("RPC_API 013 getSmartCodeEvent");

		try {
			OntTest.logger().step("测试getSmartCodeEvent()");
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map b1 = (Map)OntTest.sdk().getConnect().sendRawTransactionPreExec(invokeTx.toHexString());

//			String hash = "b94747e8fffcc4c619ca702becf04301e277d7c5e3048c01dc1f27844dad65c7";
	        String hash = toString().valueOf(invokeTx.hash());
			Object SmartCodeEvent = OntTest.sdk().getRpc().getSmartCodeEvent(hash);
			System.out.println(SmartCodeEvent);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_014_getBlockHeightByTxHash() throws Exception {
		OntTest.logger().description("RPC_API 014 getBlockHeightByTxHash");

		try {
			OntTest.logger().step("测试getBlockHeightByTxHash()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			int height0 = OntTest.sdk().getRpc().getBlockHeight();
			System.out.println("height0 = "+height0);
			System.out.println(txhash);
			Thread.sleep(8000);
			
			int height = OntTest.sdk().getRpc().getBlockHeightByTxHash(txhash);
			System.out.println(height);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_015_getMerkleProof() throws Exception {
		OntTest.logger().description("RPC_API 015 getMerkleProof");

		try {
			OntTest.logger().step("测试getMerkleProof()");

			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			System.out.println(txhash);
			Thread.sleep(8000);
			
			Object MerkleProof = OntTest.sdk().getRpc().getMerkleProof(txhash);
			System.out.println(MerkleProof);
			
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_base_016_sendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 016 sendRawTransaction");

		try {
			OntTest.logger().step("测试sendRawTransaction()");

			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        boolean RawTransaction = OntTest.sdk().getRpc().sendRawTransaction(invokeTx.toHexString());
			System.out.println(RawTransaction);
			
			assertEquals(true,RawTransaction);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	//待修改
	@Test
	public void test_base_017_sendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 017 sendRawTransaction");

		try {
			OntTest.logger().step("测试sendRawTransaction()");

			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction transaction = OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        boolean RawTransaction = OntTest.sdk().getRpc().sendRawTransaction(transaction);
			System.out.println(RawTransaction);
			
			assertEquals(true,RawTransaction);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_018_sendRawTransactionPreExec() throws Exception {
		OntTest.logger().description("RPC_API 018 sendRawTransactionPreExec");

		try {
			OntTest.logger().step("测试sendRawTransactionPreExec()");

			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
	        Map rawTransaction = (Map)OntTest.sdk().getRpc().sendRawTransactionPreExec(invokeTx.toHexString());
			System.out.println(rawTransaction);
			String ret = (String) rawTransaction.get("Result");
			
			assertEquals(true,ret.equals("01"));
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_base_019_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 019 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			Thread.sleep(5000);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(ret1);
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			System.out.println(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_normal_020_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 020 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			Thread.sleep(5000);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(ret1);
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			System.out.println(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}	
	
	@Test
	public void test_normal_021_getAllowance() throws Exception {
		OntTest.logger().description("RPC_API 021 getAllowance");

		try {
			OntTest.logger().step("测试getAllowance()");
			
			Account acc1 = OntTest.common().getAccount(0);
			Account acc2 = OntTest.common().getAccount(1);
			String addr1 = acc1.getAddressU160().toBase58();
			String addr2 = acc2.getAddressU160().toBase58();

			String ret0 = OntTest.sdk().nativevm().ont().sendApprove(acc1,addr2, 1L, acc1, 20000L,0L);
			Thread.sleep(5000);
			long ret1 = OntTest.sdk().nativevm().ont().queryAllowance(addr1, addr2);
			System.out.println(ret1);
			String exp = String.valueOf(ret1);
			
			String Allowance = OntTest.sdk().getRpc().getAllowance("ont",addr1,addr2);
			System.out.println(Allowance);
			assertEquals(true,Allowance.equals(exp));	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_022_getMemPoolTxCount() throws Exception {
		OntTest.logger().description("RPC_API 022 getMemPoolTxCount");

		try {
			OntTest.logger().step("测试getMemPoolTxCount()");
			
			Object MemPoolTxCount = OntTest.sdk().getRpc().getMemPoolTxCount();
			System.out.println(MemPoolTxCount);
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_023_getMemPoolTxState() throws Exception {
		OntTest.logger().description("RPC_API 023 getMemPoolTxState");

		try {
			OntTest.logger().step("测试getMemPoolTxState()");
			
			Account acc = OntTest.common().getAccount(0);
			String addr = acc.getAddressU160().toBase58();
			String txhash = OntTest.sdk().nativevm().ont().sendTransfer(acc, addr, 100L, acc, 20000L, 0L);
			Object MemPoolTxState = OntTest.sdk().getRpc().getMemPoolTxState(txhash);
			System.out.println(MemPoolTxState);
			assertEquals(true,true);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
	
	@Test
	public void test_base_024_syncSendRawTransaction() throws Exception {
		OntTest.logger().description("RPC_API 024 syncSendRawTransaction");

		try {
			OntTest.logger().step("测试syncSendRawTransaction()");
			
			Map ret_deploy = OntTest.api().contract().deployContract("resources/neo/invoke_neo/invoketest.cs", null);
			String codeAddr = String.valueOf(ret_deploy.get("address"));
			codeAddr = Helper.reverse(codeAddr);
			System.out.println(codeAddr);//智能合约地址
			
	        List list = new ArrayList<Object>();
	        list.add("test".getBytes());
	        List args = new ArrayList<Object>();
	        args.add(Helper.hexToBytes("01"));
	        list.add(args);
	        String payerAddr = OntTest.common().getAccount(0).getAddressU160().toBase58();
	        byte[] params = BuildParams.createCodeParamsScript(list);
	        
	        InvokeCode invokeTx = OntTest.sdk().vm().makeInvokeCodeTransaction(codeAddr, null, params, payerAddr, OntTest.sdk().DEFAULT_GAS_LIMIT, 0);
	        Transaction transaction = OntTest.sdk().signTx(invokeTx, new Account[][]{{OntTest.common().getAccount(0)}});
			
			Map sync = (Map) OntTest.sdk().getRestful().syncSendRawTransaction(invokeTx.toHexString());
			System.out.println("sync = "+sync);
			int state = (int) sync.get("State");
			
			assertEquals(true,state==1);	
		} catch(Exception e) {
			System.out.println(e);
			OntTest.logger().error(e.toString());
			fail();
		}
	}
}
	
