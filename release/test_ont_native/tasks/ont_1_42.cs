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
        struct State
        {
            public byte[] From;
            public byte[] To;
            public int Amount;
        }
        
        struct StateSend
        {
            public byte[] Send;
            public byte[] From;
            public byte[] To;
            public int Amount;
        }

        // public static readonly byte[] form = "TGfS7kPrJzdN9iA55LCezaKDjKh9L4kLBH".ToScriptHash();
        // public static readonly byte[] to = "TWd6eX917rgrB5UUG1fUoDg66Nbiv4gzkA".ToScriptHash();
        // public static readonly byte[] send = "TGfS7kPrJzdN9iA55LCezaKDjKh9L4kLBH".ToScriptHash();

        public static readonly byte[] from = null;
        public static readonly byte[] to = null;
        public static readonly byte[] send = null;


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

        public static object TransferInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            from = args[0].ToString().ToScriptHash();
            to = args[1].ToString().ToScriptHash();
            int amount = (int)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transfer", param);
        }

        public static object ApproveInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            from = args[0].ToString().ToScriptHash();
            to = args[1].ToString().ToScriptHash();
            int amount = (int)args[2];
            
            object[] param = new object[1];
            param[0] = new State { From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "approve", param);
        }

        public static object TransferFromInvoke(object[] args)
        {
            byte[] address = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 };
            send = args[0].ToString().ToScriptHash();
            from = args[1].ToString().ToScriptHash();
            to = args[2].ToString().ToScriptHash();
            int amount = (int)args[3];
            
            object[] param = new object[1];
            param[0] = new StateSend { Send = send, From = from, To = to, Amount = amount };
            
            return Native.Invoke(0, address, "transferFrom", param);
        }

    }
}
