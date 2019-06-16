import chardet
str_gbk="我们".encode('gbk')
print(chardet.detect(str_gbk))