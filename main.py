

class CPU:
	def __init__(self):
		self.memory = bytearray(4096)

	def load_rom(self, path):
		f = open(path, 'rb').read()
		for i, v in enumerate(f):
			self.memory[0x200+i] = v


if __name__ == '__main__':
	c = CPU()
	c.load_rom('data/test_opcode.ch8')
	print(c.memory)