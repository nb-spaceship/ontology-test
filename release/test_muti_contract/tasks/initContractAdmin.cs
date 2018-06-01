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
        public struct initContractAdminParam
        {
            public byte[] adminOntID;
        }

        [Appcall("ff00000000000000000000000000000000000006")]//ScriptHash
        public static extern byte[] AuthContract(string op, object[] args);

        public static object Main(string operation, params object[] args)
        {
            if (operation == "init")
            {
                return init(args);
            }

            if (operation == "A")
            {
                return A();
            }
            
            if (operation == "B")
            {
                return B();
            }

            if (operation == "C")
            {
                return C();
            }
            
            return false;
        }

        public static bool init(object[] args)
        {
            object[] _args = new object[1]; 

            initContractAdminParam param;
            param.adminOntID = (byte[]) args[0];

            _args[0] = Neo.SmartContract.Framework.Helper.Serialize(param);
            byte[] ret = AuthContract("initContractAdmin", _args);

            return ret[0] == 1;
        }

        public static int A()
        {
            return 1 + 1;
        }

        public static int B()
        {
            return 1 + 2;
        }

        public static int C()
        {
            return 2 + 2;
        }

    }
}
