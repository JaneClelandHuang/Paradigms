class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    grid1: (0 for [i..dimension])
	grid2: (0 for [i..dimension])
 
    board: [@grid1,@grid2]

    xgrid: (0 for [1..100])
	
    drawGrid: => 
        console.log "Drawing it now"       
        for cell,i in @grid1
	        console.log "Position" + i + grid i
        
gameboard = new GameBoard 10
console.log "hello"
#console.log gameboard.grid1
#console.log gameboard.grid2
#console.log gameboard.xgrid


	

		
		
