gameboard = 
    spaces = for x in [0...10]
        y = [0,0,0,0,0,0,0,0,0,0]
    setMarker: (x, y, m) =>
	    spaces[x][y] = m
    display: => 
	    console.log @spaces
	
gameboard.setMarker(4,4,3)
gameboard.display

#console.log gameboard.spaces