class HashTable(object):
	def __init__(self, size):
		self.li = [None for _ in range(size)]
		self.cur_size = 0

	def _hash(self, key):
		return hash(key) % len(self.li) # so it can index into our list

	def set(self, key, value):
		if self.cur_size >= len(self.li):
			return False # table is full
		idx = self._hash(key)
		if self.li[idx] is None:
			self.li[idx] = (key, value)
			self.cur_size +=1
			return True
		else:
			k, v = self.li[idx]
			if k == key:
				# overwrite the value but don't increase the size of the table
				self.li[idx] = (key, value)
				return True
			# probing downwards
			cur_idx = idx + 1
			while cur_idx != idx and self.li[idx] is not None:
				k, v = self.li[idx]
				if k == key:
					self.li[idx] = (key, value)
					return True
				cur_idx = 0 if cur_idx + 1 == len(self.li) else cur_idx + 1
			if cur_idx == idx:
				return False # we should never get here as we should have returned False in the size check at the beginning
			self.li[cur_idx] = (key, value)
			self.cur_size +=1
			return True

	def get(self, key):
		idx = self._hash(key)
		if self.li[idx] is None:
			return None
		k, v = self.li[idx]
		if k == key:
			return v
		cur_idx = idx + 1
		while cur_idx != idx and self.li[cur_idx] is not None:
			k, v = self.li[cur_idx]
			if k == key:
				return v
		# didnt find it because the whole list was searched or we got to a bucket that was null
		return None	

	def delete(self, key):
		idx = self._hash(key)
		if self.li[idx] == None:
			return None
		k, v = self.li[idx]
		if k == key:
			self.li[idx] = None
			self.cur_size-=1
			return v
		else:
			cur_idx = idx + 1
			while cur_idx != idx and self.li[cur_idx] is not None:
				k, v = self.li[cur_idx]
				if k == key:
					self.li[cur_idx] = None
					self.cur_size -=1
					return v
			return None # wasn't found


	def load(self):
		return self.cur_size / len(self.li)

if __name__ == '__main__':
	# hashmap tests
	hash_table = HashTable(10)
	assert hash_table.load() == 0
	assert hash_table.set(5, 10)
	assert hash_table.set(4, 9)
	assert hash_table.load() == 0.2
	assert hash_table.get(4) == 9
	assert hash_table.get(5) == 10
	assert hash_table.get(10) == None
	assert hash_table.delete(4) == 9
	assert hash_table.get(4) == None
	assert hash_table.load() == 0.1
	# collision tests

