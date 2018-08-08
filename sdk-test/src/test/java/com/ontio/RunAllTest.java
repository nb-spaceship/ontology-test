package com.ontio;

import org.junit.runner.Request;
import org.junit.runner.Result;
import org.apache.commons.lang.ArrayUtils;
import org.junit.runner.JUnitCore;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

import java.lang.reflect.Method;
import java.util.HashSet;
import java.util.Set;

import org.junit.runners.Suite.SuiteClasses;

import com.alibaba.fastjson.JSONObject;
import com.ontio.scene.Sample;
import com.ontio.testtool.utils.Common;

@RunWith(Suite.class)
@SuiteClasses({Sample.class})
public class RunAllTest {
    public static void main(String[] args) throws ClassNotFoundException {
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
        prarameter_t = "base";
        prarameter_c = "Sample"; 
        prarameter_f = "Sample.test_base_002_Sample";
        
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
        	String[] cases = prarameter_f.split(",");
        	for (String _case : cases){
        		_excludes.add(_case.split(".")[1]);
            }
        }
        
        if (!prarameter_c.equals("")){	
        	JSONObject _json = Common.loadJson(prarameter_c);
        	Set<String> keys = _json.keySet();
        	for (String _key : keys) {
        		if (_json.getString(_key).equals(true)) {
        			_files.add(prarameter_c);
        		}
        	}
        }
        
        
        
        Class<?> testClass = Sample.class;
        Method[] methods = testClass.getMethods();
        JUnitCore junitRunner = new JUnitCore();
        
        Method[] all_methods = (Method[]) ArrayUtils.addAll(null, methods);
        Method[] mymethods = new Method[all_methods.length];
        int i = 0;
        
        for (Method method : all_methods) {
        	if (method.isAnnotationPresent(org.junit.Test.class)) {
	        	System.out.println(_types.toString());
	        	
	        	if (method.getName().equals("test_init")) {
	        		mymethods[i++] = method;
	        		continue;
	        	}
	        	
	        	if (!_excludes.isEmpty() && _excludes.contains(method.getName())){
	        		continue;
	        	}
	        	
	        	String[] typeLen = method.getDeclaringClass().getTypeName().split("\\.");
	        	String m_file = typeLen[typeLen.length-1].toString();
	        	System.out.println(m_file);
	        	
	        	if (_types.contains(method.getName().split("_")[1].toString())) {
	        		if (_files.isEmpty() || _files.contains(m_file)) {
	        			mymethods[i++] = method;
		        		continue;
	        		}
	        	}
	        	
	        	if (_methods.contains(method.getName())) {
	        		if (_files.isEmpty() || _files.contains(m_file)) {
	        			mymethods[i++] = method;
		        		continue;
	        		}
	        	}
	        	
        	}
        }
                
        //TestSuite suite = new TestSuite()
        //suite.addTest(new JUnit4TestAdapter(Test1.class));
        
        for (int j = 0; j < i; j++)  {
        	Method method = mymethods[j];
            if (!method.equals(null) && method.isAnnotationPresent(org.junit.Test.class)) {
                Request request = Request.method(testClass, method.getName());
                System.out.println(method.getName());
                Result result = junitRunner.run(request);
                System.out.println(result.wasSuccessful());
            }
            
        }
    }
	
}

/*
class MethodNameFilter extends Filter {
    private final Set<String> excludedMethods = new HashSet<String>();
    public MethodNameFilter(String[] includeSheets, String[] includeTypes, String[] filterCases, String[] excludedMethods) {
        if (excludedMethods != null && excludedMethods.length != 0){
        	for(String method : excludedMethods) {
                this.excludedMethods.add(method);
            }
        }
        
        if (includeSheets != null && includeSheets.length != 0){
        	for(String includeSheet : includeSheets) {
                this.includeSheets.add(includeSheet);
            }
        }
        
        if (includeTypes != null && includeTypes.length != 0){
        	for(String includeType : includeTypes) {
                this.includeTypes.add(includeType);
            }
        }
        
        if (filterCases != null && filterCases.length != 0){
        	for(String filterCase : filterCases) {
                this.filterCases.add(filterCase);
            }
        }
    	
    }
    
    @Override
    public boolean shouldRun(Description description) {
        String methodName = description.getMethodName();
        if(excludedMethods.contains(methodName)) {
            return false;
        }
        return true;
    }
    
    @Override
    public String describe() {
        return this.getClass().getSimpleName() + "-excluded methods: " + 
                excludedMethods;
    }
}
*/
