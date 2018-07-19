# -*- coding:utf-8 -*-
import os
import sys
import logging
import paramiko
import hashlib
import json

sys.path.append('..')

#from utils.selfig import selfig
from utils.logger import LoggerInstance as logger
from utils.hexstring import *
from utils.error import Error
from utils.api.commonapi import *
from utils.config import Config

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handle = logging.FileHandler("init_selfcheck.log", mode="w")
handle.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handle.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(level=logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handle)
logger.addHandler(console)

def sftp_transfer(_from, _to, _node_index, _op="get"):
    # on local host
    if _node_index == 0:
        cmd = "cp -rf " + _from + " " + _to
        os.system(cmd)
        return 

    private_key = paramiko.RSAKey.from_private_key_file("./resource/id_rsa", "367wxd")

    transport = paramiko.Transport((Config.NODES[_node_index]["ip"] , 22))

    transport.connect(username="ubuntu", pkey=private_key)

    sftp = paramiko.SFTPClient.from_transport(transport)

    if _op == "put":
        sftp.put(_from, _to)
    elif _op == "get":
        sftp.get(_from, _to)
    else:
        logger.error("operation not supported")

    transport.close()

def calc_md5_for_file(_file):
    md5 = hashlib.md5()
    with open(_file, "rb") as f:
        md5.update(f.read())
    return md5.hexdigest()

def calc_md5_for_files(_folder):
    md5 = []
    files = os.listdir(_folder)
    files.sort()
    for _file in files:
        md5.append(str(calc_md5_for_file(os.path.join(_folder, _file))))
    return md5

def calc_md5_for_folder(folder):
  md5 = hashlib.md5()
  files = os.listdir(folder)
  files.sort()
  for _file in files:
    md5.update(str(calc_md5_for_file(os.path.join(folder, _file))).encode())
  return md5.hexdigest()


class InitConfig():
    def __init__(self):
        self.initconfig = {}
    
    def get_init_config(self):
        with open("config.json") as f:
            cf = json.load(f)

        self.initconfig["ontology_source_path"] = cf["resource"]["root"] + cf["resource"]["ontology_source_name"]
        self.initconfig["wallet_source_path"] = cf["resource"]["root"] + cf["resource"]["wallet_source_name"]
        self.initconfig["onto_config_source_path"] = cf["resource"]["root"] + cf["resource"]["onto_config_source_name"]
        self.initconfig["test_config_source_path"] = cf["resource"]["root"] + cf["resource"]["test_config_source_name"]
        self.initconfig["sigsvr_source_path"] = cf["resource"]["root"] + cf["resource"]["sigsvr_source_name"]
        self.initconfig["abi_source_path"] = cf["resource"]["root"] + cf["resource"]["abi_source_name"]
        
        self.initconfig["node_path"] = cf["node"]["root"] + cf["node"]["onto_name"]
        self.initconfig["wallet_path"] = cf["node"]["root"] + cf["node"]["wallet_name"]
        self.initconfig["onto_config_path"] = cf["node"]["root"] + cf["node"]["onto_config_name"]
        self.initconfig["sigsvr_path"] = cf["node"]["root"] + cf["node"]["sigsvr_name"]
        self.initconfig["abi_path"] = cf["node"]["root"] + cf["node"]["abi_name"]

        self.initconfig["test_config_path"] = cf["test_config_path"]



class SelfCheck():
    def __init__(self, initconfig):
        self.nodecounts = len(Config.NODES)

        self.ontology_source_path = initconfig["ontology_source_path"]
        self.wallet_source_path = initconfig["wallet_source_path"]
        self.onto_config_source_path = initconfig["onto_config_source_path"]
        self.test_config_source_path = initconfig["test_config_source_path"]
        self.sigsvr_source_path = initconfig["sigsvr_source_path"]
        self.abi_source_path = initconfig["abi_source_path"]


        self.node_path = initconfig["node_path"]
        self.wallet_path = initconfig["wallet_path"]
        self.onto_config_path = initconfig["onto_config_path"]
        self.test_config_path = initconfig["test_config_path"]
        self.sigsvr_path = initconfig["sigsvr_path"]
        self.abi_path = initconfig["abi_path"]

        self.ontology_correct_md5 = str(calc_md5_for_file(self.ontology_source_path))
        self.wallet_correct_md5 = calc_md5_for_files(self.wallet_source_path)
        self.onto_config_md5 = str(calc_md5_for_file(self.onto_config_source_path))
        self.test_config_md5 = str(calc_md5_for_file(self.test_config_source_path))
        self.sigsvr_md5 = str(calc_md5_for_file(self.sigsvr_source_path))
        self.abi_md5 = str(calc_md5_for_folder(self.abi_source_path))


    def check_ontology(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes ontology\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " ontology......")
            response = get_version_ontology(i)
            if "doesnot exists" in response["result"] or (response["result"]["md5"] != self.ontology_correct_md5):
                logger.error("node " + str(i+1) + " ontology version error or not exists")
                logger.info("start transfer ontology from node 1 to node " + str(i+1))
                sftp_transfer(self.ontology_source_path, self.node_path, i, "put")
                logger.info("transfer ontology OK ")
            
            check_xmode_ontology(i)

            logger.info("checking node " + str(i+1) + " ontology OK\n")

        logger.info("checking all nodes ontology OK")
        logger.info("----------------------------------\n\n")

    def check_wallet(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes wallets\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " wallet......")
            response = get_version_wallet(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.wallet_correct_md5[i]):
                logger.error("node " + str(i+1) + " wallet version error or not exists")
                logger.info("start transfer wallet from node 1 to node " + str(i+1))
                wallet_index = "0" + str(i+1) if i < 10 else str(i)
                sftp_transfer(self.wallet_source_path+"/wallet_"+wallet_index+".dat", self.wallet_path, i, "put")
                logger.info("transfer wallet OK ")

            logger.info("checking node " + str(i+1) + " wallet OK\n")

        logger.info("checking all nodes wallets OK")
        logger.info("----------------------------------\n\n")
        
    def check_onto_config(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes ontology config\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " ontology config......")
            response = get_version_onto_config(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.onto_config_md5):
                logger.error("node " + str(i+1) + " ontology config version error or not exists")
                logger.info("start transfer ontology config from node 1 to node " + str(i+1))
                sftp_transfer(self.onto_config_source_path, self.onto_config_path, i, "put")
                logger.info("transfer ontology config OK ")

            logger.info("checking node " + str(i+1) + " ontology config OK\n")

        logger.info("checking all nodes ontology config OK")
        logger.info("----------------------------------\n\n")

    def check_test_config(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes test config\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " test config......")
            response = get_version_test_config(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.test_config_md5):
                logger.error("node " + str(i+1) + " test config version error or not exists")
                logger.info("start transfer test config from node 1 to node " + str(i+1))
                sftp_transfer(self.test_config_source_path, self.test_config_path, i, "put")
                logger.info("transfer test config OK ")

            logger.info("checking node " + str(i+1) + " test config OK\n")

        logger.info("checking all nodes test config OK")
        logger.info("----------------------------------\n\n")


    def check_sigsvr(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes sigsvr\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " sigsvr......")
            response = get_version_sigsvr(i)
            if "doesnot exists" in response["result"] or (response["result"]["md5"] != self.sigsvr_md5):
                logger.error("node " + str(i+1) + " sigsvr version error or not exists")
                logger.info("start transfer sigsvr from node 1 to node " + str(i+1))
                sftp_transfer(self.sigsvr_source_path, self.sigsvr_path, i, "put")
                logger.info("transfer sigsvr OK ")
            
            check_xmode_sigsvr(i)

            logger.info("checking node " + str(i+1) + " sigsvr OK\n")

        logger.info("checking all nodes sigsvr OK")
        logger.info("----------------------------------\n\n")

    def check_abi(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes abi\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " abi......")
            response = get_version_abi(i)
            if "doesnot exists" in response["result"] or (response["result"] != self.abi_md5):
                logger.error("node " + str(i+1) + " abi version error or not exists")
                logger.info("start transfer abi from node 1 to node " + str(i+1))
                sftp_transfer(self.abi_source_path, self.abi_path, i, "put")
                logger.info("transfer abi OK ")

            logger.info("checking node " + str(i+1) + " abi OK\n")

        logger.info("checking all nodes abi OK")
        logger.info("----------------------------------\n\n")

    def check_tools(self):
        logger.info("----------------------------------")
        logger.info("start checking all nodes tools\n")

        for i in range(self.nodecounts):
            logger.info("checking node " + str(i+1) + " tools......")
            
            response = check_xmode_tools(i)
            if isinstance(response["result"], str) and "doesnot exists" in response["result"]:
                logger.error(response["result"])

            logger.info("checking node " + str(i+1) + " tools OK\n")

        logger.info("checking all nodes tools OK")
        logger.info("----------------------------------\n\n")

    def check_all(self):
        self.check_ontology()
        self.check_wallet()
        self.check_sigsvr()
        self.check_onto_config()
        self.check_test_config()
        self.check_abi()
        # self.check_tools()


if __name__ == "__main__":
    # get config
    initconfig = InitConfig()
    initconfig.get_init_config()

    selfcheck = SelfCheck(initconfig.initconfig)
    selfcheck.check_all()


    
