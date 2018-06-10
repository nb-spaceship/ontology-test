import os
import shutil

for i in range(105, 138):
    shutil.copyfile("104_withdraw.json", str(i)+"_withdraw.json")

