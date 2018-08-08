package com.ontio.testtool.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

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
}
