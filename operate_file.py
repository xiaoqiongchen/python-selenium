import os
import re
from General import Common
class operate_file(object):

    def read_test_data(self,file_path):#读测试数据
        test_data=[]
        if os.path.exists(file_path):
           with open(file_path,"r",encoding="utf-8") as fp:
                temp=fp.readlines()
                for line in temp:
                    test_data.append(eval(line.strip()))
           return test_data
        else:
             return False

    def read_test_step_data(self,file_path):#读测试步骤数据
        test_step_data=[]
        if os.path.exists(file_path):
            with open(file_path,"r",encoding="utf-8") as fp:
                temp=fp.readlines()
                for line in temp:
                    datalist=line.strip().split("||")
                    templist=[]
                    for  data in range(len(datalist)):
                         templist.append(datalist[data])
                    test_step_data.append(templist)
            return test_step_data
        else:
             return False

    def eval_commands(self,operate_test_data,operate_test_step_data):
        General=Common()
        for test_data in operate_test_data:
            for test_step_data in operate_test_step_data:
                if len(test_step_data)==1:
                   command=test_step_data[0]+"()"
                elif len(test_step_data)==2:
                   command=test_step_data[0]+"('"+test_step_data[1]+"')"
                elif len(test_step_data)==3:
                   command=test_step_data[0]+"('"+test_step_data[1]+"','"+test_step_data[2]+"')"
                elif len(test_step_data)==4:
                   keyword="".join(re.findall(r"^\$\{(.*?)\}",test_step_data[3]))
                   command = test_step_data[0] + "('" + test_step_data[1] + "','" + test_step_data[2] + "','"+test_data[keyword]+"')"
                print("General."+command)
                eval("General."+command)