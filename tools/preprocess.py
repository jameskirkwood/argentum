from scanner_base import ScannerBase, ap, re

ap.add_argument('FILE', help='main assembly source file')
args = ap.parse_args()

class Scanner(ScannerBase):

	def scan_line(self, line):
		for m in self.accept(r'^\s*\.(\w+):(.*)$', line):
			print(f':{self.symbol}_{m.group(1)}')
			self.scan_line(m.group(2))
			return
		for m in self.accept(r'^\s*([^\s;][^;]*?)\s*(;.*)?$', line):
			if hasattr(self, 'symbol'):
				print(re.sub(r'\.(\w+)', self.symbol + '_\\1', m.group(1)))
			else:
				print(m.group(1))
	
	def directive_symbol(self, spec):
		for m in self.accept(r'^(\w+)\s*:\s*(.*?)\s*"\s*(.*?)"$', spec):
			if hasattr(self, 'namespace'):
				self.symbol = self.namespace + m.group(1)
			else:
				self.symbol = m.group(1)
			print(':' + self.symbol)
			return
		raise RuntimeError('invalid symbol directive')

Scanner(args)
