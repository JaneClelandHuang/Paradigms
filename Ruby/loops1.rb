strings = ["one", "two", "four", "five"]
strings.inject(0) do |sum, str|
    #next if str.size == 4
    #sum + str.size
	next sum if str.size == 4
end