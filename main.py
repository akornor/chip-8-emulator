

class CPU:
	def __init__(self):
		self.memory = bytearray(4096)

		## registers
		self.V = [] # Vx
		self.I = 0 # index
		self.ST = 0 # sound timer
		self.DT = 0 # delay timer
		self.PC = 0 # program counter
		self.SP = 0 # stack pointer
		self.stack = []

	def load_rom(self, path):
		f = open(path, 'rb').read()
		for i, v in enumerate(f):
			self.memory[0x200+i] = v


if __name__ == '__main__':
	c = CPU()
	c.load_rom('data/test_opcode.ch8')
	print(c.memory)