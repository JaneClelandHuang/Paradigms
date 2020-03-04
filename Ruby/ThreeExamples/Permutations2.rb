if ARGV.length != 1 
    STDERR.puts 'Exactly one argument is required' 
    exit 1 
end 
ARGC[0].chars.permutation.each{|s| puts s.join}