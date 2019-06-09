import argparse, re, os

ap = argparse.ArgumentParser()
ap.add_argument('-I', '--include_path', nargs=1, action='append', default=[],
	help='append to include search path')

class ScannerBase(object):

	def accept(self, pattern, string):
		match = re.match(pattern, string)
		return [match] if match else []

	def __init__(self, args, filename=None):
		if filename == None: filename = args.FILE
		self.directory = os.path.dirname(filename)
		self.includes = sum(args.include_path, [])
		self.args = args
		for line in open(filename, 'r'):
			for m in self.accept(r'^\s*[#\.](\w+)\s+(.*?)\s*(?:;.*)?$', line):
				name, rest = m.groups()
				if hasattr(self, 'directive_' + name):
					getattr(self, 'directive_' + name)(rest)
					break
			else:
				self.scan_line(line)
	
	def scan_line(self, name):
		pass

	def resolve_quoted_filename(self, filename):
		p = os.path.join(self.directory, filename)
		if os.path.exists(p): return p
		for path in self.includes:
			p = os.path.join(path, filename)
			if os.path.exists(p): return p
		if os.path.exists(filename): return filename
		raise RuntimeError(filename + ' could not be resolved')

	def directive_include(self, rest):
		for m in self.accept(r'^("?)(.*)\1$', rest):
			type(self)(self.args,
				filename=self.resolve_quoted_filename(m.group(2)))
			return
		raise RuntimeError('malformed include directive')

	def directive_namespace(self, spec):
		for m in self.accept(r'^"(.*)"$', spec):
			self.namespace = m.group(1)
			return
		raise RuntimeError('invalid namespace directive')
