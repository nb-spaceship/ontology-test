using Neo.SmartContract.Framework.Services.Neo;

namespace Neo.SmartContract
{
    public class Lock : Framework.SmartContract
    {
        public static object Main(string operation)
        {
            switch (operation)
            {
                case "test_neo_return_53":
                    return test_neo_return_53();
                default:
                    return false;
            }
        }

        public static string test_neo_return_53()
        {
            return "qwertyuiop";
        }  
    }
}