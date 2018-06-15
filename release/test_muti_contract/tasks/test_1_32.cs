using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public class AppContract : SmartContract
    {
        public struct InitContractAdminParam
        {
            public byte[] adminOntID;
        }
        
        public struct VerifyTokenParam
        {
            public byte[] ContractAddr;
            public byte[] Caller;
            public string Fn;
            public int KeyNo;
        }

		//did:ont:
		 public static readonly byte[] mAdminOntID = { 
                0x64, 0x69, 0x64, 0x3a, 0x6f, 0x6e, 0x74, 0x3a,
				0x41, 0x65, 0x34, 0x70, 0x4b, 0x5a, 0x31, 0x73, 0x69,
				0x50, 0x67, 0x70, 0x4c, 0x66, 0x42, 0x33, 0x57, 0x51,
				0x38, 0x6a, 0x4d, 0x51, 0x38, 0x58, 0x62, 0x54, 0x54,
				0x67, 0x53, 0x32, 0x33, 0x64, 0x56, 0x50};
				
        public static readonly byte[] authContractAddr = {
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x06 };
		
		
        public static object Main(string operation, object[] token,  object[] args)
        {
            if (operation == "init")
            {
                return init();
            }

            if (operation == "A")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return A();
            }

            if (operation == "B")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return B();
            }

            if (operation == "C")
            {
                //we need to check if the caller is authorized to invoke foo
                if (!VerifyToken(operation, token)) return false;

                return C();
            }
    
            return operation;
        }

        public static object A()
        {
            return "A";
        }

        public static object B()
        {
            return "B";
        }

        public static object C()
        {
            return "C";
        }

        public static bool InitContractAdmin(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] adminOntID = (byte[])args[0];
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = adminOntID };
            byte[] res = Native.Invoke(0, address, "initContractAdmin", param);
            return res[0] == 1;
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            byte[] contractAddr = ExecutionEngine.ExecutingScriptHash;
            byte[] caller = (byte[])token[0];
            string fn = operation;
            int keyNo = (int)token[1];
            
            object[] param = new object[1];
            param[0] = new verifyTokenParam { ContractAddr = contractAddr, Caller = caller, Fn = fn, KeyNo = keyNo };
            byte[] res = Native.Invoke(0, address, "verifyToken", param);
            return true;
        }

    }
}
