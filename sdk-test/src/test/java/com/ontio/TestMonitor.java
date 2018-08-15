package com.ontio;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.junit.runner.Description;
import org.junit.runner.Result;
import org.junit.runner.notification.RunListener;

import com.ontio.testtool.OntTest;

public class TestMonitor extends RunListener {
	
	public static List<Description> failedDescription = new ArrayList<Description>();
	
	@Override
    public void testRunStarted(Description description) throws Exception {
		failedDescription.clear();
		
        System.out.println("Number of tests to execute: " + description.testCount());
    }
	
	@Override
    public void testRunFinished(Result result) throws Exception {
        System.out.println("Number of tests executed: " + result.getRunCount());
    }
	
	@Override
    public void testStarted(Description description) throws Exception {
        System.out.println("Starting: " + description.getMethodName());
    }
	
	@Override
    public void testFinished(Description description) throws Exception {
    	
    	File logPath = OntTest.logger().logfile();
    	String contents = "";
		String line = "";
		try {
			BufferedReader in = new BufferedReader(new FileReader(logPath));
			line=in.readLine();
			while (line!=null) {
				contents = contents + line;
				line=in.readLine();
			}
			in.close();
		} catch (IOException e) {
			e.printStackTrace(); 
		}
		// TODO
		if (false) {
			failedDescription.add(description);
		}
    	
        System.out.println("Finished: " + description.getMethodName());
    }

}
