
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

##### answer
# from string import maketrans

# a = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

# b = 'abcdefghijklmnopqrstuvwxyz'

# c = 'cdefghijklmnopqrstuvwxyzab'

# d = maketrans(b,c)

# print a.translate(d)

# print 'map'.translate(d)


