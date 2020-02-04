class GameBoard
  constructor: (dimension) ->
    @dimension = dimension

  @grid = for x in [0...dimension]
    for y in [0...dimension]
        grid(x, y) = "0"

gameboard = new GameBoard
gameboard.grid
	

		
		
