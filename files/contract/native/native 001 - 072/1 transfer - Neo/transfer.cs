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
        public struct TransferParam
        {
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }
        public struct ApproveParam
        {
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }
        public struct TransferFromParam
        {
            public byte[] send;
            public byte[] from;
            public byte[] to;
            public UInt64 amount;
        }

        [Appcall("ff00000000000000000000000000000000000001")]//ScriptHash
        public static extern byte[] ONT(string op, object[] args);

        public static object Main(string operation, params object[] args)
        {
            if (operation == "transfer")
            {
                return TransferInvoke(args);
            }
            
            if(operation == "approve")
            {
                return ApproveInvoke(args);
            }
            if(operation == "transferFrom")
            {
                return TransferFromInvoke(args);
            }

            return false;
        }

        public static bool TransferInvoke(object[] args)
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

        public static bool ApproveInvoke(object[] args)
        {
            ApproveParam approveParam;
            approveParam.from = (byte[])args[0];
            approveParam.to = (byte[])args[1];
            approveParam.amount = (UInt64)args[2];
            
            object[] approveArgs = new object[1];
            approveArgs[0] = approveParam.Serialize();
            
            byte[] ret = ONT("approve", approveArgs);
            return ret[0] == 1;
        }

        public static bool TransferFromInvoke(object[] args)
        {
            TransferFromParam transferFromParam;
            transferFromParam.send = (byte[])args[0];
            transferFromParam.from = (byte[])args[1];
            transferFromParam.to = (byte[])args[2];
            transferFromParam.amount = (UInt64)args[3];
            
            object[] transferFromArgs = new object[1];
            transferFromArgs[0] = transferFromParam.Serialize();
            
            byte[] ret = ONT("transferFrom", transferFromArgs);
            return ret[0] == 1;
        }

    }
}
