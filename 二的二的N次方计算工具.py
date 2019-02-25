#/usr/bin/env python
#python3
#二的二的N次方计算工具

a=0  #记录平方次数
b=2  #存平方后的数

while a>=0:  #死循环部分
	a=a+1
	b=pow(b,2)
	print('当前循环次数为:',a,'\n')
	print('当前平方后的值为:',b,'\n')
	c=str(a)  #次数转字符串存文件
	d=str(b)  #数字转字符串存文件
	f=open('number.txt','a')
	f.write('当前循环次数为:')
	f.write(c)
	f.write('\n')
	f.write('当前平方后的值为:')
	f.write(d)
	f.write('\n')
	f.close()
