# Example 1:
[a, b, c] = [1, 2, 3] 
 
bad = -> 	# clobbers outer a
    a = 10 
	 
okay = -> 	# writes to local b
    ((b) -> b = 20)() 
 
better = -> # writes to local c
    do (c=30) ->  

bad(); okay(); better() 
assert = require 'assert' 
assert.deepStrictEqual([a,b,c], [10,2,3]) 

# Example 2:
assert = require 'assert'
assert 4.toFixed(2) is '4.00'
assert true.toString() is 'true'
assert 'abcde'.length is 5
assert [5,3,9,4,6].indexOf(3) is 1
assert.throws((-> null.toString()), TypeError)
assert.throws((->undefined.toString()), TypeError)

assert 78.8? is true
assert false? is true
assert []? is true
assert undefined? is false
assert null? is false
x = 9;
assert x? is true
