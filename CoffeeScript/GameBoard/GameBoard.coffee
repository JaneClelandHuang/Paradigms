class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    grid1: (0 for [1..10])
    grid2: (0 for [1..10])
    xgrid: [@grid1,@grid1]
	
	
        
gameboard = new GameBoard 10
console.log "hello"
console.log gameboard.grid1
console.log gameboard.grid2
console.log gameboard.xgrid


	

		
		
