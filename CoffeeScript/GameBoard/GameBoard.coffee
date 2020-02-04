class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    @grid1: [0 for [0..10]]
    @grid2: [0 for [0..10]]
    @xgrid: [[0 for [0..10]],[0 for [0..10]]]
	
    displayBoard: -> 
    console.log "Current Grid"
    console.log "" + @grid1
    console.log "" + @grid2
	console.log "" + @xgrid
		       
gameBoard = new GameBoard 10
console.log GameBoard.displayBoard

	

		
		
