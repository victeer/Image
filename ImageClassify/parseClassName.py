#!/usr/bin/python
#encoding: utf-8
#read file from tml,
import codecs
'''
label file is just like between
- - - - -
menjin:门襟:17
三粒 双排扣 多粒 单排扣 两粒 一粒 三粒 系带 暗扣 拉链 一粒扣 牛角扣 套头 多扣 无扣 斜拉链门襟 前中拉链门襟

'''

class  parseClassName():

    @staticmethod
    def getClass(label_file_path):
        '''
            [classNameMap,className_dict]=def getClass(label_file_path):
        '''
        className_dict={}
        className={}
        tmpClass=None
        with codecs.open(filename=label_file_path,mode='r',encoding="gb2312") as f:#,encoding="gb2312"
            for line in f:
                tmp=line.strip()
                #if tmp is empty
                if len(tmp)==0:
                    continue
                else:
                    #first line: the big class and its subclass number
                    if tmpClass==None:
                        #print tmp
                        t=tmp.split(':')

                        tmpClass=t[0]
                        print tmpClass
                        className[t[0]]=t[1]
                        number=int(t[2])
                    else:
                        className_dict[tmpClass]=tmp.split(' ')
                        if number!=len(className_dict[tmpClass]):
                            print tmpClass," class number is not match","number is ",number," len is ",len(className_dict[tmpClass])
                        tmpClass=None
                        number=0
        for str in className_dict:
            print str," :",#,className_dict[str]#[i for i in  className_dict[str]],className_dict[str]
            for i in className_dict[str]:
                print i,
            print
        return className,className_dict


     #将10个图片进行的预测结果相加得到的值，进行排序得到最终的结果。

if __name__=="__main__":
    parseClassName.getClass("C:\\Users\\Victor\\Downloads\\tml")