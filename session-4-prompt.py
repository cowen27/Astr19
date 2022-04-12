class Animal:
	def __init__(self, arm_len, leg_len, num_eyes, has_tail, is_furry):
		self.arm_len = float(arm_len)
		self.leg_len = float(leg_len)
		self.num_eyes = int(num_eyes)
		self.has_tail = bool(has_tail)
		self.is_furry = bool(is_furry)

	def print_description(self):
		print("Arm length:", self.arm_len)
		print("Leg length:", self.leg_len)
		print("Number of eyes:", self.num_eyes)
		print("Has a tail:", self.has_tail)
		print("Is furry:", self.is_furry)

def main():
	monkey = Animal(30, 34, 2, True, True)
	monkey.print_description()

if __name__ == '__main__':
	main()
