def get_largest_n(input, n, low, high):
    if(n<=1): return ''
    string = input[low:high] if high != 0 else input[low:]
    largest = ''
    index = 0
    for i,c in enumerate(string):
        if c > largest:
            largest = c
            index = i
    
    return largest+str(get_largest_n(input, n-1, index+1+low, -(n-3)))
    

p1 = 0
with open("input.in") as f:
    for line in f:
        output = ""
        line = line.strip()
    
        output += get_largest_n(line, 12, 0, -11)
        print(output)
        p1 += int(output)
print(p1)