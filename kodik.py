filter_list = lambda l: [x for x in l if type(x) != str]
print(filter_list([1,2,'aasf','1','123',123]))