import numpy as np

# (2, 3, 4)
a = np.array([
	[
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]
	],
	[
		[13, 14, 15, 16],
		[17, 18, 19, 20],
		[21, 22, 23, 24]
	]
])

print(a)

print("Shape if the array := {}".format(a.shape))

print("Length of array := {}".format(len(a)))

print("Length of array[0] := {}".format(len(a[0])))

print("Length of array[0] := {}".format(len(a[0][1])))

print("----------------------------------")
print(a[:, 1, 3])
