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
        [Appcall("ff00000000000000000000000000000000000001")]//ScriptHash
        public static extern byte[] ONT(string op, object[] args);

        public struct TransferParam
        {
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }

        public static object Main(string operation, object[] args)
        {
           if (operation == "contractA_Func_A")
           {
               bool yes = ContractA_Func_A(args);
               if( yes ) return "ContractA_Func_A invoke success";
           }
           return false;
        }

        public static bool ContractA_Func_A(object[] args)
        {
            TransferParam transferParam;
            transferParam.from = (byte[])args[0];
            transferParam.to = (byte[])args[1];
            transferParam.amount = (UInt64)args[2];
            
            object[] transferArgs = new object[1];
            transferArgs[0] = transferParam.Serialize();
            
            byte[] ret = ONT("transfer", transferArgs);
            return ret[0] == 1;
        }
    }
}