class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    @_grid1: [0 for [1..10]]
    @_grid2: (0 for [1..10])
    @_xgrid: [@grid1,@grid1]
	
	@displayBoard: => 
        console.log "Hello"
        console.log(@grid1)
        console.log(@grid2)
		
        
GameBoard.displayBoard

	

		
		
