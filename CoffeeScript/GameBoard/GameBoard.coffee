class GameBoard
    constructor: ->

    @grid0: [0 for [0..10]]
    @grid1: [0 for [0..10]]
    @grid2: [0 for [0..10]]
    @grid3: [0 for [0..10]]
    @grid4: [0 for [0..10]]
    @grid5: [0 for [0..10]]
    @grid6: [0 for [0..10]]
    @grid7: [0 for [0..10]]
    @grid7: [0 for [0..10]]
    @grid9: [0 for [0..10]]

	
    displayBoard: -> 
    console.log "" + @grid0
    console.log "" + @grid1
    console.log "" + @grid2
    console.log "" + @grid3
    console.log "" + @grid4
    console.log "" + @grid5
    console.log "" + @grid6
    console.log "" + @grid7
    console.log "" + @grid8
    console.log "" + @grid9
	
gameBoard = new GameBoard 10
console.log GameBoard.displayBoard

	

		
		
