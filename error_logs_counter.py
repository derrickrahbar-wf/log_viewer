with open("logs.txt") as f:
    content = f.readlines()

self_exception = False
error_dict = dict()
for line in content:
	if self_exception:
		print line
		if line in error_dict:
			error_dict[line] = error_dict[line] + 1
		else:
			error_dict[line] = 1
		self_exception = False
	if "raise" in line:
		self_exception = True

print error_dict