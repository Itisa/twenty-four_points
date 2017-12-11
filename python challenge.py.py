
########## level 0
# a = 2
# for z in range(37):
# 	a *= 2
# print a

########## level 1

##### my writing

# c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# a = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr..q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
# b = []
# # i hope you didnt transport it by hand. thats what computers are 
# print a
# # print c
# # print c.index(c[-1])
# for z in range(len(a)):
# 	if a[z] == ' ':
# 		b.append(' ')
# 	elif a[z] == '.':
# 		b.append('.')
# 	elif c.index(a[z]) == 24:
# 		b.append('a')
# 	elif c.index(a[z]) == 25:
# 		b.append('b')
	
# 	else:
# 		b.append(c[ c.index(a[z]) + 2 ])

# print ''.join(b)
# # for z1 in range(len(b)):
# # 	print b[z1],
# 	# print ''
#8JQP8QPUR

##### answer
# from string import maketrans

# a = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

# b = 'abcdefghijklmnopqrstuvwxyz'

# c = 'cdefghijklmnopqrstuvwxyzab'

# d = maketrans(b,c)

# print a.translate(d)

# print 'map'.translate(d)

########## level 2

# c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# b = []
# a = 'level 2'
# for z in range(len(a)):
# 	if a[z] in c:
# 		b.append(a[z])
# print ''.join(b)

########## level 3

# a = 'level 3'
# c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# d=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# b = []
# for z in range(len(a)):
# 	if a[z] in c:
# 		if a[z-1] in d and a[z-2] in d and a[z-3] in d and a[z+1] in d and a[z+2] in d and a[z+3] in d and a[z-4] in c and a[z+4] in c:
# 			b.append(a[z])
# print ''.join(b)

########## level 4

##### my writing
# -24 ~ mx
# ms ~ -1
# mx =    9223372036854775784
# ms =   -9223372036854775807
# lilen = 9223372036854775808
# print mx+ms

##### answer
# import urllib2
# import re 


# pattern = re.compile(r'\d+')

# x = 82930
# for z in range(400):
# 	b = []
# 	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % x
# 	a = urllib2.urlopen(url)
# 	a = a.read()
# 	y =''.join(re.findall(pattern,a))
# 	x = int(y)
# 	print x

###answer is 66831

########## level 5

import cPickle

a = 'E:\\sub work\\24\\txt\\level 5.txt'
with open(a,'r') as f:
	data = cPickle.load(f)
	# print data
	print len(data)
	for z in data:
		print z
# print b,len(b),b[1]
# for z in range(len(b)):
# 	if b[z] == 'l' and b[z+1] == 'p':
# 		print b[z],b[z+1],b[z+2],b[z+3],b[z+4]







