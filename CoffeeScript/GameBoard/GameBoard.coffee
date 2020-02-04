class GameBoard
    constructor: (dimension) ->
        @dimension = dimension

    grid: [
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

    xgrid: (0 for [1..100])
	
	#x2grid: ([i, 1] for i in [1])[[ 1, 1 ]]
    
	myArray: {{[0 for [1..10],[0 for [1..10]}}
	
    drawGrid: => 
        console.log "Drawing it now"       
        for cell,i in @grid
	        console.log "Position" + i + grid i
        
gameboard = new GameBoard 10
console.log "hello"
console.log gameboard.grid.length
gameboard.drawGrid
console.log gameboard.grid
console.log gameboard.xgrid
console.log gameboard.myArray


	

		
		
