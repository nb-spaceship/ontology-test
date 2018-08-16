package com.ontio;

import java.util.HashSet;
import java.util.Set;

import org.junit.runner.Description;
import org.junit.runner.manipulation.Filter;

public class MethodNameFilter extends Filter {
    private final Set<String> excludedMethods = new HashSet<String>();
    private final Set<String> includeTypes = new HashSet<String>();
    private final Set<String> filterCases = new HashSet<String>();
    
    public MethodNameFilter(Set<String> includeSheets, Set<String> includeTypes, Set<String> filterCases, Set<String> excludedMethods) {
        if (excludedMethods != null && excludedMethods.size() != 0){
        	for(String method : excludedMethods) {
                this.excludedMethods.add(method);
            }
        }
        
        if (includeTypes != null && includeTypes.size() != 0){
        	for(String includeType : includeTypes) {
                this.includeTypes.add(includeType);
            }
        }
        
        if (filterCases != null && filterCases.size() != 0){
        	for(String filterCase : filterCases) {
                this.filterCases.add(filterCase);
            }
        }
    	
    }
    
    @Override
    public boolean shouldRun(Description description) {
    	
        String methodName = description.getMethodName();
        
        if (methodName.equals("test_init")) {
        	return true;
    	}
        
        if (!excludedMethods.isEmpty() && excludedMethods.contains(methodName)){
        	return false;
    	}
            	
    	if (filterCases.isEmpty() && (includeTypes.isEmpty() || includeTypes.contains(methodName.split("_")[1].toString()))) {
    		return true;
    	}
    	
    	if (includeTypes.isEmpty() && (filterCases.isEmpty() || filterCases.contains(methodName))) {
			return true;
    	}
        return false;
        
    }
    
    @Override
    public String describe() {
        return "";
    }
    
}