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
                case "GetTransaction_Attribute":
                    return GetTransaction_Attribute((byte[])args[0]);
                default:
                    return false;
            }
        }

        public static TransactionAttribute[] GetTransaction_Attribute(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            TransactionAttribute[] attr = tran.GetAttributes(); 
            return attr;
        }
    }
}

// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c3176765745472616e73616374696f6e417474726962757465876306006218006c766b51c300c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756654c56b6c766b00527ac4616c766b00c361681d4e656f2e426c6f636b636861696e2e4765745472616e73616374696f6e6c766b51527ac46c766b51c361681d4e656f2e5472616e73616374696f6e2e476574417474726962757465736c766b52527ac46c766b52c36c766b53527ac46203006c766b53c3616c7566

// Deploy contract:
//   Contract Address:TMgBgv5zjQTjCNj1bLB1nEeFExFbYPymyi
//   TxHash:623c92daaaf0a279e0c360402fc9581d3fc67d0389b22c3a26b77e9feab9c75e

// Tip:
//   Using './ontology info status 623c92daaaf0a279e0c360402fc9581d3fc67d0389b22c3a26b77e9feab9c75e' to query transaction status


