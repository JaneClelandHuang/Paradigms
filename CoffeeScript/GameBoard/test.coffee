spaces = for x in [0...10]
    y=[0 for [0..10]]

setMarker: (x, y, m) =>
    [x][y] = m

display: =>
    console.log spaces
	
setMarker(4,4,3)
display

#console.log gameboard.spaces