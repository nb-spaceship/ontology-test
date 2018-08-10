package com.ontio.testtool.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.OntSdk;
import com.github.ontio.sdk.manager.WalletMgr;
import com.github.ontio.sdk.wallet.Wallet;
import com.ontio.testtool.OntTest;

public class Common {
	public static JSONObject loadJson(String filepath) {
		String fileName = filepath;
		String contents = "";
		String line = "";
		try {
			BufferedReader in = new BufferedReader(new FileReader(fileName));
			line=in.readLine();
			while (line!=null) {
				contents = contents + line;
				line=in.readLine();
			}
			in.close();
		 } catch (IOException e) {
			e.printStackTrace(); 
		 }
		
		JSONObject jobj = JSON.parseObject(contents);

		return jobj;
	}
	
	public static com.github.ontio.account.Account getDefaultAccount(WalletMgr walltemgr) {
	    try {
		    com.github.ontio.sdk.wallet.Account accountInfo = walltemgr.getDefaultAccount();
		    if (accountInfo == null) {
		    	 System.out.println("no default wallet..");
		    	 return null;
		    }
			return walltemgr.getAccount(accountInfo.address, Config.PWD, accountInfo.getSalt());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    
	    return null;
	}
	
	public static com.github.ontio.account.Account getAccount(int index) {
		try {
			if (Config.TEST_MODE == true) {
				WalletMgr wm = new WalletMgr(Config.nodeWallet(0), OntTest.sdk().defaultSignScheme);
				Wallet w = wm.getWalletFile();
				List<com.github.ontio.sdk.wallet.Account> accountinfos = w.getAccounts();
		        System.out.println("init ont&ong in test mode: " + accountinfos.size());
		        if (accountinfos.size() <= index) {
		        	OntTest.logger().error("Get account: index out of range " + index);
		        	return null;
		        }
		        com.github.ontio.sdk.wallet.Account accountinfo = accountinfos.get(index);
		        return wm.getAccount(accountinfo.address, Config.PWD);
			} else {
				WalletMgr wm = new WalletMgr(Config.nodeWallet(index), OntTest.sdk().defaultSignScheme);
		        com.github.ontio.sdk.wallet.Account accountinfo = wm.getDefaultAccount();
		        return wm.getAccount(accountinfo.address, Config.PWD);
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
}
