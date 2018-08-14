package com.ontio;

import org.junit.runner.Request;
import org.junit.runner.Result;
import org.junit.runner.manipulation.Filter;
import org.junit.runner.notification.RunNotifier;
import org.apache.commons.lang.ArrayUtils;
import org.junit.runner.Description;
import org.junit.runner.JUnitCore;

import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Method;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import com.ontio.MethodNameFilter;

import com.alibaba.fastjson.JSONObject;
import com.ontio.sdkapi.Claim;
import com.ontio.sdkapi.ClaimRecord;
import com.ontio.sdkapi.DigitalAccount;
import com.ontio.sdkapi.DigitalIdentity;
import com.ontio.sdkapi.Invoke;
import com.ontio.sdkapi.MnemonicCodesStr;
import com.ontio.sdkapi.ONG_Native;
import com.ontio.sdkapi.ONT_Native;
import com.ontio.sdkapi.Ontid;
import com.ontio.sdkapi.RPC_API;
import com.ontio.testtool.OntTest;

public class RunAllTest {
    public static void main(String[] args) throws ClassNotFoundException {
    	OntTest.init();
    	
    	String prarameter_c = "";  
    	String prarameter_t = "";  
    	String prarameter_f = "";  
    	String prarameter_e = "";  
    	
    	int optSetting = 0;  
        for (; optSetting < args.length; optSetting++) {  
            if ("-c".equals(args[optSetting]) || "--config".equals(args[optSetting])) {  
            	prarameter_c = args[++optSetting];  
            } else if ("-t".equals(args[optSetting]) || "--type".equals(args[optSetting])) {  
            	prarameter_t = args[++optSetting];  
            } else if ("-f".equals(args[optSetting]) || "--filter".equals(args[optSetting])) {  
            	prarameter_f = args[++optSetting];  
            } else if ("-e".equals(args[optSetting]) || "--exclude".equals(args[optSetting])) {  
            	prarameter_e = args[++optSetting];  
            }  
        }
        
        // prarameter_t = "base";  
        // prarameter_f = "ClaimRecord.test_abnormal_002_exportIdentityQRCode";  
        // prarameter_c = "C:\\Users\\tpc\\Desktop\\a.json";
        // prarameter_e = "Sample.test_base_001_Sample1";
        
        Set<String> _classes = new HashSet<String>();
        Set<String> _methods = new HashSet<String>();
        Set<String> _excludes = new HashSet<String>();
        Set<String> _types = new HashSet<String>();
        Set<String> _files = new HashSet<String>();
        
        if (!prarameter_f.equals("")){
        	String[] cases = prarameter_f.split(",");
            for (String _case : cases){
            	_classes.add(_case.split("\\.")[0]);
            	_methods.add(_case.split("\\.")[1]);
            }
        }
        
        if (!prarameter_t.equals("")){
        	if (prarameter_t.equals("base")) {
        		_types.add("base");
        	} else if (prarameter_t.equals("normal")){
        		_types.add("base");
        		_types.add("normal");
        	} else if (prarameter_t.equals("abnormal")){
        		_types.add("abnormal");
        	}
        }
        
        if (!prarameter_e.equals("")){
        	String[] cases = prarameter_e.split(",");
        	for (String _case : cases){
        		_excludes.add(_case.split("\\.")[1]);
            }
        }
        
        if (!prarameter_c.equals("")){	
        	JSONObject _json = OntTest.common().loadJson(prarameter_c);
        	Set<String> keys = _json.keySet();
        	for (String _key : keys) {
        		if (_json.getString(_key).equals(true)) {
        			_files.add(prarameter_c);
        		}
        	}
        }
        // System.out.println(_files.toString());
        
        List<Class<?>> all_class = new ArrayList<Class<?>>();
        all_class.add(Claim.class);
        all_class.add(ClaimRecord.class);
        all_class.add(DigitalAccount.class);
        all_class.add(DigitalIdentity.class);
        all_class.add(Invoke.class);
        all_class.add(MnemonicCodesStr.class);
        all_class.add(ONG_Native.class);
        all_class.add(ONT_Native.class);
        all_class.add(RPC_API.class);
        all_class.add(Ontid.class);
        
        JUnitCore junitRunner = new JUnitCore();
        junitRunner.addListener(new TestMonitor());
        for (Class<?> _class : all_class) {
	        Request request = Request.aClass(_class);
	        request = request.filterWith(new MethodNameFilter(_files, _types, _methods,_excludes));
	        request = request.sortWith(new Comparator<Description>(){
				@Override
				public int compare(Description d1, Description d2) {
					if (d1.getClassName().equals(d2.getClassName())) {
						return d1.getMethodName().split("_")[2].toString().compareTo(d2.getMethodName().split("_")[2].toString());
					} else {
						return d1.getClassName().compareTo(d1.getClassName());
					}
				}
	        });
	        
	        Result result = junitRunner.run(request);
	        System.out.println(result.wasSuccessful());
        }
        /*
        Method[] all_methods = null;
        for (Class<?> testClass : all_class) {
        	all_methods = (Method[]) ArrayUtils.addAll(all_methods, testClass.getMethods());
        }
        
        
        Method[] tmpmethods = new Method[all_methods.length];
        
        JUnitCore junitRunner = new JUnitCore();
        int i = 0;
        
        for (Method method : all_methods) {
        	if (method.isAnnotationPresent(org.junit.Test.class)) {
	        	// System.out.println(_types.toString());
	        	
	        	if (method.getName().equals("test_init")) {
	        		tmpmethods[i++] = method;
	        		continue;
	        	}
	        	
	        	if (!_excludes.isEmpty() && _excludes.contains(method.getName())){
	        		continue;
	        	}
	        	
	        	String[] typeLen = method.getDeclaringClass().getTypeName().split("\\.");
	        	String m_file = typeLen[typeLen.length-1].toString();
	        	
	        	System.out.println(method.getName().split("_")[1].toString());
	        	
	        	if (_methods.isEmpty() && (_types.isEmpty() || _types.contains(method.getName().split("_")[1].toString()))) {
	        		if (_files.isEmpty() || _files.contains(m_file)) {
	        			tmpmethods[i++] = method;
		        		continue;
	        		}
	        	}
	        	
	        	if (_types.isEmpty() && (_methods.isEmpty() || _methods.contains(method.getName()))) {
	        		if (_files.isEmpty() || _files.contains(m_file)) {
	        			tmpmethods[i++] = method;
		        		continue;
	        		}
	        	}
	        	
        	}
        }
        
        Method[] mymethods = new Method[i];
        for (int j = 0; j < i; j++) {
        	if (tmpmethods[j] != null) {
        		mymethods[j] = tmpmethods[j];
        	}
        	else {
        		break;
        	}
        }
        
        Arrays.sort(mymethods, new Comparator<Method>(){
			@Override
			public int compare(Method m1, Method m2) {
				if (m1.getDeclaringClass().getName().equals(m2.getDeclaringClass().getName())) {
					return m1.getName().split("_")[2].toString().compareTo(m2.getName().split("_")[2].toString());
				} else {
					return m1.getDeclaringClass().getName().compareTo(m2.getDeclaringClass().getName());
				}
			}
        });
        
        for (Method m : mymethods) {
        	System.out.println(m.getDeclaringClass().getName());
        	System.out.println(m.getName().split("_")[2].toString());
        }
                
        // Sleep(200000); 
        long startTime = System.currentTimeMillis();
        long endtime = startTime;
        long costtime = 0;
        SimpleDateFormat dateformat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        String lastClass = "";
        for (int j = 0; j < i; j++)  {
        	try {
	        	Method method = mymethods[j];
	        	if (j == 0 || !lastClass.equals(method.getDeclaringClass().getName())) {
	        		startTime = System.currentTimeMillis();
	        	}
	        	
	            // if (!method.equals(null) && method.isAnnotationPresent(org.junit.Test.class)) 
	            if (true) {
	                // Request request = Request.method(method.getDeclaringClass(), method.getName());
	            	Request request = Request.aClass(all_class.get(0));
	            	request.filterWith(new MethodNameFilter(_methods,_excludes,_types, _files));
	                System.out.println(method.getName());
	                Result result = junitRunner.run(request);
	                System.out.println(result.wasSuccessful());
	            }
	
	        	lastClass = method.getDeclaringClass().getName();
	            endtime = System.currentTimeMillis();
	            costtime = endtime - startTime;
	            String reportstr ="[time]" + "\n" +
						"start=" + dateformat.format(startTime) + "\n" +
						"end=" + dateformat.format(endtime)  + "\n" +
						"cost=" + (costtime / 1000);
	            String repotepath = OntTest.logger().logfile().getParentFile().getAbsolutePath() + "/report.ini";
				FileWriter reportFileWriter = new FileWriter(repotepath, false);
				reportFileWriter.write(reportstr);
				reportFileWriter.close();
        	}
        	catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }*/
    }
	
}


