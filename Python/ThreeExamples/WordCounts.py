import sys, re 
sys.stderr.write('Hello')
counts = {} 
print(sys.stdin)
for line in sys.stdin: 
    for word in re.findall(r'[a-z\']+', line.lower()):
        print(word)    
        #counts[word] = counts.get(word, 0) + 1 
#for word, count in sorted(counts.items()): 
#    print(word, count)