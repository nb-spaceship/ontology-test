using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Example
{
    public struct initContractAdminParam
    {
        public byte[] adminOntID;
    }

    public class AppContract : SmartContract
    {
       
        [Appcall("ff00000000000000000000000000000000000006")]
        public static extern byte[] AuthContract(string op, object[] args);

        public static Object Main(string operation, object[] args)
        {
            if (operation == "initContractAdmin") 
                return init(args[0]);
            
            if (operation == "initContractAdmin_004")
            {
                bool isSuccess;
                isSuccess = init(args[0]);
                isSuccess = init(args[1]);
                return isSuccess;
            } 
                
            return false;
        }

        public static bool init(object arg)
        {
            object[] _args = new object[1];

            initContractAdminParam param;
            param.adminOntID = (byte[])arg;

            _args[0] = Neo.SmartContract.Framework.Helper.Serialize(param);
            byte[] ret = AuthContract("initContractAdmin", _args);

            return ret[0] == 1;
        }
    }
}
