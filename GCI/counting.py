import csv


dic = {}

def r():
	f = open('ref_col.csv', 'r')
	r = csv.reader(f)

	for row in r:
		data = row[7]
		if data in dic:
			dic[data] += 1
		else:
			dic[data] = 1 

	pair = dic.items()
	d_sorted = sorted(pair, key=lambda x: x[1], reverse=True)

	for i in d_sorted:
		print(i)

r()

# 	return dic

# d = r()


# pair = d.items()
# d_sorted = sorted(pair, key=lambda x: x[1], reverse=True)


# def w():
# 	fn = open('csv/manufacturer.csv', 'w')
# 	w = csv.writer(fn)
	 
# 	w.writerows(d_sorted)
# 	fn.close()



# w()








