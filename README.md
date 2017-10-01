### kpcb-hashtable
Hash table implementation that supports set(), get(), delete(), and load(). 

### Running the program
I used `python3`. The program and tests can be run with the command `python3 hash_table.py`.

### Implementation details:
- set() is implemented by obtaining the index by running the key through a hash function and modding the result by the maximum length of the hash table. Collisions are handled by linearly probing downwards (wrapping across the top of the table if need be). During linear probing, if an empty slot exists, the item is inserted there. 
- Note: set(), if called with the same key twice, the second call will overwrite the value of the first call. That is, set(3, 4) followed by set(3, 5) followed by get(3) will result in 5 and no errors.
- get() is implemented similar to set() - an index is obtained, and then we (possibly) probe linearly downwards until we find the correct key (or return None if it doesn't exist)
- delete() is implemented similar to get(), except it also decreases the size of the hash table. 
- load() gives us a sense of how full our hash table is. As the load factor approaches 1 (the table fills up), the hash table operations take longer, as there is an increased chance of collisions (so we spend more time probing downwards)