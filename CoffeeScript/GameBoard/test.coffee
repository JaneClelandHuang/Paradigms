class GameBoard = [
    spaces = for x in [0...10]
        y = [1,1,1,1,1,1,1,1]

    setMarker: (x, y, m) => spaces[x][y] = m
	
gameboard = new GameBoard
gameboard.setMarker(4,4,X)

console.log gameboard.spaces