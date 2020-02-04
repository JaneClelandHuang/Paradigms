class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    @grid1: [0 for [1..10]]
    @grid2: [0 for [1..10]]
    @xgrid: [@_grid1,@_grid1]
	
    displayBoard: -> 
    console.log "Hello"
    console.log "Grid 1" + @grid1
    console.log(@grid2)
	console.log(@xgrid)
		       
gameBoard = new GameBoard 10
console.log GameBoard.displayBoard

	

		
		
