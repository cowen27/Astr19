import numpy as np

def print_table(vals):
	for x in vals:
		print(f'{x} | {np.sin(x)}')

def main():
	#vals = np.arange(2*np.pi, dtype=float)
	vals = np.linspace(0, 2*np.pi, 1000).astype(list)
	print_table(vals)

if __name__ == '__main__':
	main()