def sum_float(x, y):
	sum = x + y
	print(sum, type(sum))

def diff_int(x, y):
	diff = x - y
	print(diff, type(diff))

def product_mix(x, y):
	product = x * y
	print(product, type(product))

def main():
	print("Sum of Floats")
	sum_float(float(input("Float 1: ")), float(input("Float 2: ")))
	print()

	print("Difference of Integers")
	diff_int(int(input("Integer 1: ")), int(input("Integer 2: ")))
	print()

	print("Product of Float and Integer")
	product_mix(float(input("Float: ")), int(input("Integer: ")))

if __name__ == '__main__':
	main()