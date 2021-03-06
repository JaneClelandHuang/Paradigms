reader = require('readline').createInterface process.stdin, null
counts = new Map()

reader.on 'line', (line) ->
    for word in (line.toLowerCase().match(/[a-z']+/g) or [])
        counts.set word, (counts.get(word) or 0) + 1
	
reader.on 'close', ->
    for word in Array.from(counts.keys()).sort()
        console.log "#{word} #{counts.get word}"
		
		