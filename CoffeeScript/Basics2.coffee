# Example 1:
[a, b, c] = [1, 2, 3] 
 
bad = -> 	# clobbers outer a
    a = 10 
	 
okay = -> 	# writes to local b
    ((b) -> b = 20)() 
 
better = -> # writes to local c
    do (c=30) -> # clobbers outer a 

bad(); okay(); better() 
assert = require 'assert' 
assert.deepStrictEqual([a,b,c], [10,2,3]) 