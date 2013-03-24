class lst1:
    def lst(self,lst1):
	self.lst1=lst1
	return self.lst1
class lst2:
    def lst(self,lst2):
	self.lst2=lst2
	return self.lst2
class main(lst1,lst2):
    def __init__(self):
	pass
    def method(self,list1,list2):
	x=lst1.lst(self,list1)
	y=lst2.lst(self,list2)
	print x
	print y
	x.append(y)
	print 'After appending'
	print x
a=main()
a.method([1,2,3,4],[5,6,7,8])
