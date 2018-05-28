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
                case "GetContract_Destroy":
                    return GetContract_Destroy();
                default:
                    return false;
            }
        }

        public static bool GetContract_Destroy()
        {
             Contract.Destroy();
             return true;
        }
    }
}

// 54c56b6c766b00527ac46c766b51527ac4616c766b00c36c766b52527ac46c766b52c313476574436f6e74726163745f4d69677261746587630600621100616521006c766b53527ac4620e00006c766b53527ac46203006c766b53c3616c756651c56b616168144e656f2e436f6e74726163742e44657374726f7961516c766b00527ac46203006c766b00c3616c7566

// Deploy contract:
//   Contract Address:TMeMsaAu3C72eqv6PGGS4iZLGCEWrxxpdS
//   TxHash:f746b008b7568793892ed0a4469eb9a387418aa437ac0e09cef9f353d95c7719

// Tip:
//   Using './ontology info status f746b008b7568793892ed0a4469eb9a387418aa437ac0e09cef9f353d95c7719' to query transaction status
