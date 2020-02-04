# Example 1:
# Code produces baz, baz, and baz.
# How would you fix it? 
alerters = [];



for i in ['foo', 'bar', 'baz']
    alerters.push 
    -> console.log(i)

for alerter in alerters
    alerter()
 
 