fakeObject.upto(40) do |c| 
    fakeObject.upto(c - 1) do |b| 
        fakeObject.upto(b - 1) do |a| 
            puts "#{a}, #{b}, #{c}" if a * a + b * b == c * c 
        end 
    end 
end 
