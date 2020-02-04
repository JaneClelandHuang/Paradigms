class GameBoard
  constructor: (dimension) ->
    @dimension = dimension

  @grid = for x in [0...@dimension]
    for y in [0...@dimension]
	    new Elements.Space(x, y)
        #grid(x, y) = "0"


gameboard = new GameBoard(10)
gameboard.grid
	

		
		
