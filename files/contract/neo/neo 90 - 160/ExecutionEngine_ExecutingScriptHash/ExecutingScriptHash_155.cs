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
                case "ExecutingScriptHash":
                    return GetExecutingScriptHash();
                default:
                    return false;
            }
        }
        
        public static byte[] GetExecutingScriptHash()
        {
            return ExecutionEngine.ExecutingScriptHash;
        }
    }
}