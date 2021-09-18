# wapf to find fact of an integer

def fact(num):
	f = 1
	for i in range(1, num+1):
		f = f * i
	return f

n = 12
r = 2

perm = fact(n) / fact(n-r)
comb = fact(n) / (fact(r) * fact(n-r))

print("perm = ", perm)
print("comb = ", comb)

# dev karo ek baar.. call karo baar baar
# DRY ==> dont repeat yourself