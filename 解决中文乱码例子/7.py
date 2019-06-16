str_utf8="我们".encode('utf-8')
str_gbk=str_utf8.decode('utf-8')
str_gbk1=str_gbk.encode('gbk')
print(str_gbk1)
