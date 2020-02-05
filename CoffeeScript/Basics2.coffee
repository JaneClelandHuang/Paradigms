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

# Example 3:
employees = [ 
    {name: 'alice', salary: 85000} 
    {name: 'bob', salary: 77500} 
    {name: 'chi', salary: 58200} 
    {name: 'dinh', salary: 99259} 
    {name: 'ekaterina', salary: 105882} 
    {name: 'fahima', salary: 79999}] 
 
assert = require 'assert' 
highEarners = (e.name for e in employees when e.salary > 80000) 
shortNames = (e.name for e in employees when e.name.length < 4) 
console.log("High earners: ", highEarners)
console.log("Short names: ", shortNames)

assert.deepStrictEqual highEarners, ['alice', 'dinh', 'ekaterina'] 
assert.deepStrictEqual shortNames, ['bob', 'chi'] 
