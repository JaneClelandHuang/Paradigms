class GameBoard 
    spaces = for x in [0...10]
        y = [1,1,1,1,1,1,1,1]

    setMarker: (x, y, m) => spaces[x][y] = m
	
    display: => console.log spaces
	
gameboard = new GameBoard
gameboard.setMarker(4,4,X)
gameboard.display

#console.log gameboard.spaces