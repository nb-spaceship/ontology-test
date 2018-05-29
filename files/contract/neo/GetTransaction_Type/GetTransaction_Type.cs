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
                case "GetTransaction_Type":
                    GetTransaction_Type((byte[])args[0]);
                    return true;
                default:
                    return false;
            }
        }

        public static byte GetTransaction_Type(byte[] txid)
        {
            Transaction tran = Blockchain.GetTransaction(txid);
            return tran.Type;
        }
    }
}


// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c3126765745472616e73616374696f6e54797065876306006218006c766b51c300c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756653c56b6c766b00527ac4616c766b00c361681d4e656f2e426c6f636b636861696e2e4765745472616e73616374696f6e6c766b51527ac46c766b51c36168174e656f2e5472616e73616374696f6e2e476574547970656c766b52527ac46203006c766b52c3616c7566
	
// Contract Address:TMiU8rXBsycyMP4nQns6NnrwbVLC1qK9uq
//   TxHash:b294e5936cd430f55452d94d0b440912225974c0ccd34526c3906e667d658017

// Tip:
//   Using './ontology info status b294e5936cd430f55452d94d0b440912225974c0ccd34526c3906e667d658017' to query transaction status


    
