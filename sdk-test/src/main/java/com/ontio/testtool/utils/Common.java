package com.ontio.testtool.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.sdk.manager.WalletMgr;

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
}
