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
                case "GetContract_Create":
                    return GetContract_Create((byte[])args[0],(bool)args[1],(string)args[2],(string)args[3],(string)args[4],(string)args[5],(string)args[6]);
                default:
                    return false;
            }
        }

        public static Contract GetContract_Create(byte[] script,bool flag, string name, string version, string author, string email, string desc)
        {
            Contract cre = Contract.Create(script,flag,name,version,author,email,desc);
            return cre;
        }
    }
}

Deploy contract:
  Contract Address:TMi8efCgUugRdEkwsAvTqc29mmrsaFNyZv
  TxHash:e2c577e52215c090c5a0c951f9a2aa9e8e0d11cc2ac1e7f8a8493f43ac924fc5

Tip:
  Using './ontology info status e2c577e52215c090c5a0c951f9a2aa9e8e0d11cc2ac1e7f8a8493f43ac924fc5' to query transaction status
