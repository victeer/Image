# coding=utf8
s = "中文"
s1 = u"中文"
s2 = unicode(s, "utf8") #省略参数将用python默认的ASCII来解码
s3 = s.decode("utf8") #把str转换成unicode是decode，unicode函数作用与之相同
print len(s1),s1
print len(s2),s2
print len(s3),s3
print len(s),s


print s.decode("utf-8")
