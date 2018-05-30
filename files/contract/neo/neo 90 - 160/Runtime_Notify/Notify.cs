using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class Domain : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "Notify":
                    SendNotify((byte[])args[0]);
                    return true;
                default:
                    return false;
            }
        }
        
        public static void SendNotify(byte[] Message)
        {
            Runtime.Notify(Message);
        }
    }
}