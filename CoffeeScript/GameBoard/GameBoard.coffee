class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    grid1: [0 for [1..10]]
    grid2: (0 for [1..10])
    xgrid: [@grid1,@grid1]
	
	displayBoard: => 
        console.log "Hello"
        console.log(@grid1)
        console.log(@grid2)
		
        
gameboard = new GameBoard 10
gameboard.displayBoard

	

		
		
