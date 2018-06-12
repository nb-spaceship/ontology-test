using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public struct initContractAdminParam
    {
        public byte[] AdminOntID;
    }

    public struct verifyTokenParam
    {
        public byte[] ContractAddr;
        public byte[] Caller;
        public byte[] Fn;
        public int KeyNo;
    }
    
    public struct Transfer
    {
        public byte[] From;
        public byte[] To;
        public int Value;
    }

    public class AppContract : SmartContract
    {
      
        public static Object Main(string operation, object[] token, object[] args)
        {
            if (operation == "initContractAdmin") return InitContractAdmin(args);
            
            
            if (operation == "A")
            {
                return A(args);
            }

            return false; 
        }

        public static byte[] A(object[] args)
        {
   
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            byte[] from = (byte[])args[1];
            byte[] to = (byte[])args[2];
            int amount = (int)args[3];
            
            object[] param = new object[1];
            param[0] = new Transfer { From = from, To = to, Value = amount };

            return Native.Invoke(0, address, "transfer", param);
        }

        public static object InitContractAdmin(object[] args)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            byte[] adminOntID = (byte[])args[0];
            object[] param = new object[1];
            param[0] = new initContractAdminParam { AdminOntID = adminOntID };
            
            return Native.Invoke(0, address, "initContractAdmin", param);
        }

        public static bool VerifyToken(string operation, object[] token)
        {
            byte[] address = { 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 };
            
            byte[] contractAddr = ExecutionEngine.ExecutingScriptHash;
            byte[] caller = (byte[])token[0];
            byte[] fn = operation.AsByteArray();
            int keyNo = (int)token[1];
            
            object[] param = new object[1];
            param[0] = new verifyTokenParam { ContractAddr = contractAddr, Caller = caller, Fn = fn, KeyNo = keyNo };
            byte[] res = Native.Invoke(0, address, "verifyToken", param);
            return true;
        }
    }
}


