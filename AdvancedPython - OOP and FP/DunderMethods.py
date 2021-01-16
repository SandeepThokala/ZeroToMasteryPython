class SuperList(list):
	def __len__(self):
		return 1000
sl = SuperList()
sl.append(7)
sl.append(4)
sl.append(5)
print(sl)
print(sl[2])
print(len(sl))
print(issubclass(SuperList, list))
print(issubclass(list, object))

#=====================================

print(repr(list))

#=====================================

class BooDict(dict):
	def __getitem__(self, k):
		return 'Boo...!!'

bd = BooDict()
print(bd['l'])