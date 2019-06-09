from scanner_base import ScannerBase, ap

ap.add_argument('FILE', help='annotated assembly source file')
args = ap.parse_args()

class Scanner(ScannerBase):

	def scan_line(self, line):
		for m in self.accept(r'^.*?;;\s*(.*)$', line):
			print(m.group(1))

	def directive_symbol(self, spec):
		for m in self.accept(r'^(\w+)\s*:\s*(.*?)(\(.*?\))?\s*"\s*(.*?)"$', spec):
			name, kind, args, desc = m.groups()
			print(f'## **{kind}** `{self.namespace + name}`{args if args else ""} \n')
			print(f'> {desc}\n')
			return
		raise RuntimeError('invalid symbol directive')

Scanner(args)
