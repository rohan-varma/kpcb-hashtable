class HashTable(object):
	def __init__(self, size):
		self.li = [None * size]
		self.cur_size = 0

	def _hash(self, key):
		return hash(key) % self.cur_size

	def set(key, value):
		if self.cur_size >= len(self.li):
			return False # table is full

		idx = self._hash(key)

		if self.li[idx] is None:
			self.li[idx] = value
		else:
			# probe downwards
			cur_idx = idx + 1
			while self.li[cur_idx] is not None and cur_idx != idx:
				cur_idx = 0 if cur_idx + 1 == len(self.li) else cur_idx + 1
			self.li[cur_idx] = value
			self.cur_size += 1

		return True

	def get(key):
		pass		

	def delete(key):
		pass

	def load():
		pass
