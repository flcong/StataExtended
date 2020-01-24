import sublime
import sublime_plugin

class gtolCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Loop over all selections
		for sel in self.view.sel():
			if not sel.empty():
				# String to search local
				kw = "\\${" + self.view.substr(sel) + "}"
				# String to replace
				trg = "`" + self.view.substr(sel) + "'"
				# Find the first occurrence
				loc = self.view.find(kw, 0)
				# Loop until no matching is found
				while len(loc)>0:
					# Replace
					self.view.replace(edit, loc, trg)
					# Get the next match (starting from the current)
					loc = self.view.find(kw, loc.b)
