spaces = for x in [0...10]
    y=[0 for [0..10]]

setMarker = (x, y, m) =>
    [x][y] = m

console.log spaces
	
setMarker(4,4,3)
console.log spaces


#console.log gameboard.spaces