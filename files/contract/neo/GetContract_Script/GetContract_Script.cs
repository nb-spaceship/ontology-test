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
                case "GetContract_Script":
                    return GetContract_Script((byte[])args[0]);
                default:
                    return false;
            }
        }

        public static byte[] GetContract_Script(byte[] script_hash)
        {
            Contract cont = Blockchain.GetContract(script_hash);
            return cont.Script;
        }
    }
}

// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c312476574436f6e74726163745f536372697074876306006218006c766b51c300c3616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756653c56b6c766b00527ac4616c766b00c361681a4e656f2e426c6f636b636861696e2e476574436f6e74726163746c766b51527ac46c766b51c36168164e656f2e436f6e74726163742e4765745363726970746c766b52527ac46203006c766b52c3616c7566


// Deploy contract:
//   Contract Address:TMfVtXcrk664meQzKXicRMrqzVBBnP8BNN
//   TxHash:1c3357524c1540e88d48bdb13468a5cfa9afc47c026df3a458b163b7025212ea

// Tip:
//   Using './ontology info status 1c3357524c1540e88d48bdb13468a5cfa9afc47c026df3a458b163b7025212ea' to query transaction status
