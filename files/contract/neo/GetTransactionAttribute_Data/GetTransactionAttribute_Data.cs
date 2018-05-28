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
                case "GetTransactionAttribute_Data":
                    return GetTransactionAttribute_Data((byte[])args[0],(int)args[1]);
                default:
                    return false;
            }
        }

        public static byte[] GetTransactionAttribute_Data(byte[] txid,int index)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr[index].Data;
        }
    }
}
	
// Deploy contract:
//   Contract Address:TMi6qvzcBiQyx3AYK6N4BAcvkHiZyQHvzN
//   TxHash:6e20db1fd52b1a3e56ac848c93e406f1f0bf59712bc1add01115c93b7a52f5be

// Tip:
//   Using './ontology info status 6e20db1fd52b1a3e56ac848c93e406f1f0bf59712bc1add01115c93b7a52f5be' to query transaction status
