using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class BlockchainTest : Framework.SmartContract
    {
        public static object Main(string operation, params object[] args)
        {
            switch (operation)
            {
                case "GetHeight":
                    return GetHeight();
                case "GetHeader":
                    return GetHeader(args[0]);
                case "GetBlock":
                    return GetBlock(args[0]);
                case "GetTransaction":
                    return GetTransaction(args[0]);
                case "GetContract":
                    return GetContract(args[0]);
                case "GetHeaderHash":
                    return GetHeaderHash(args[0]);
                case "GetHeaderVersion":
                    return GetHeaderVersion(args[0]);
                case "GetHeaderPrevHash":
                    return GetHeaderPrevHash(args[0]);
                case "GetHeaderIndex":
                    return GetHeaderIndex(args[0]);
                case "GetHeaderMerkleRoot":
                    return GetHeaderMerkleRoot(args[0]);
                case "GetHeaderTimestamp":
                    return GetHeaderTimestamp(args[0]);
                case "GetHeaderConsensusData":
                    return GetHeaderConsensusData(args[0]);
                case "GetHeaderNextConsensus":
                    return GetHeaderNextConsensus(args[0]);
                case "GetBlockTransactionCount":
                    return GetBlockTransactionCount(args[0]);
                case "GetBlockTransactions":
                    return GetBlockTransactions(args[0]);
                case "GetBlockTransaction_40":
                    return GetBlockTransaction_40(args[0], args[1]);
                case "GetBlockTransaction_44":
                    return GetBlockTransaction_44(args[0]);
                case "GetBlockTransaction_45":
                    return GetBlockTransaction_45(args[0]);
                default:
                    return false;
            }
        }

        public static uint GetHeight()
        {
            return Blockchain.GetHeight();
        }

        public static Header GetHeader(object height)
        {
            uint _height = (uint)height;
            return Blockchain.GetHeader(_height);
        }

        public static Block GetBlock(object hash)
        {
            byte[] _hash = (byte[])hash;
            return Blockchain.GetBlock(_hash);
        }

        public static Transaction GetTransaction(object txid)
        {
            byte[] _txid = (byte[])txid;
            return Blockchain.GetTransaction(_txid);
        }

        public static Contract GetContract(object script_hash)
        {
            byte[] _script_hash = (byte[])script_hash;
            return Blockchain.GetContract(_script_hash);
        }

        public static byte[] GetHeaderHash(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            return header.Hash;
        }

        public static uint GetHeaderVersion(object height)
        {
            Header header = GetHeader(height);
            return header.Version;
        }

        public static byte[] GetHeaderPrevHash(object height)
        {
            Header header = GetHeader(height);
            return header.PrevHash;
        }

        public static uint GetHeaderIndex(object height)
        {
            Header header = GetHeader(height);
            return header.Index;
        }

        public static byte[] GetHeaderMerkleRoot(object height)
        {
            Header header = GetHeader(height);
            return header.MerkleRoot;
        }

        public static uint GetHeaderTimestamp(object height)
        {
            Header header = GetHeader(height);
            return header.Timestamp;
        }

        public static ulong GetHeaderConsensusData(object height)
        {
            Header header = GetHeader(height);
            return header.ConsensusData;
        }

        public static byte[] GetHeaderNextConsensus(object height)
        {
            Header header = GetHeader(height);
            return header.NextConsensus;
        }
        
        public static int GetBlockTransactionCount(object height)
        {
            Block block = GetBlockByHeight(height);
            return block.GetTransactionCount();
        }

        public static Transaction[] GetBlockTransactions(object height)
        {
            Block block = GetBlockByHeight(height);
            return block.GetTransactions();
        }

        public static Transaction GetBlockTransaction_40(object height, object index)
        {
            Block block = GetBlockByHeight(height);
            int _index = (int)index;
            return block.GetTransaction(_index);
        }

        public static Transaction GetBlockTransaction_44(object height)
        {
            Block block = GetBlockByHeight(height);
            int count = block.GetTransactionCount();
            return block.GetTransaction(count-1);
        }

        public static Transaction GetBlockTransaction_45(object height)
        {
            Block block = GetBlock(height);
            int count = block.GetTransactionCount();
            return block.GetTransaction(count);
        }

        public static Block GetBlockByHeight(object height)
        {
            uint _height = (uint)height;
            Header header = Blockchain.GetHeader(_height);
            Block block = Blockchain.GetBlock(header.Hash);
            return block;
        }
    }
}