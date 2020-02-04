class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    @grid = [
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
        0,0,0,0,0,0,0,0,0,0
    ]
	
    @drawGrid = -> 
        for i in grid
	        console.log i
        
gameboard = new GameBoard(10)
console.log "hello"
console.log gameboard.grid.length
gameboard.drawGrid
	

		
		
