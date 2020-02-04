class GameBoard
    constructor: (dimension) ->
    @dimension = dimension

    grid1: [0 for [1..10]]
    grid2: [0 for [1..10]]
    xgrid: [@_grid1,@_grid1]
	
	GameBoard.prototype.getGrid = function() 
    displayBoard: => 
    console.log "Hello"
    console.log(@_grid1)
    console.log(@_grid2)
		
        
gameBoard = new Gameboard 10
console.log GameBoard.displayBoard

	

		
		
