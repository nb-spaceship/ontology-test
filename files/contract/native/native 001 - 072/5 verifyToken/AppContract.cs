using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public struct verifyTokenParam
    {
        public byte[] contractAddr;
        public byte[] caller;
        public byte[] fn;
        public int keyNo;
    }

    public class AppContract : SmartContract
    {
       
        [Appcall("ff00000000000000000000000000000000000006")]
        public static extern byte[] AuthContract(string op, object[] args);

        public static Object Main(string operation, object[] token)
        {
            if (operation == "verifyToken")
            {
                if (!verifyToken(operation, token))
                {
                    return false;
                }
                return foo();
            }
            return false;
        }

        public static bool foo()
        {
            return true;
        }

        public static bool verifyToken(string operation, object[] token)
        {
            object[] _args = new object[1];

            verifyTokenParam param;
            param.contractAddr = (byte[])token[0];
            param.fn = (byte[])token[1];
            param.caller = (byte[])token[2];
            param.keyNo = (int)token[3];

            _args[0] = param.Serialize();
            byte[] ret = AuthContract("verifyToken", _args);

            return ret[0] == 1;
        }
    }
}
