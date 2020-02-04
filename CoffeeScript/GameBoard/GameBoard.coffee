class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    @_grid1: [0 for [1..10]]
    @_grid2: (0 for [1..10])
    #@_xgrid: [@_grid1,@_grid1]
	
    displayBoard: => 
        console.log "Hello"
        console.log(@_grid1)
        console.log(@_grid2)
		
        
GameBoard.displayBoard
console.log GameBoard.displayBoard

	

		
		
