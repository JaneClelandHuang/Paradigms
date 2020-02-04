gameboard =
    spaces = for x in [0...10]
        y = [0,0,0,0,0]

    name: 'Alice'
    tryToSayHelloButFail: (delay) ->
        setTimeout (() -> console.log "Hi from #{@name} :("), delay
    sayHello: (delay) ->
        setTimeout (() => console.log "Hi from #{@name} :)"),delay

gameboard.tryToSayHelloButFail 1000 # Hi from undefined :(
gameboard.sayHello 1000 #Hi from Alice :)