upto(40) do |c| 
    upto(c - 1) do |b| 
        upto(b - 1) do |a| 
            puts "#{a}, #{b}, #{c}" if a * a + b * b == c * c 
        end 
    end 
end 
