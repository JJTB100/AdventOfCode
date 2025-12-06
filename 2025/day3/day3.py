def get_largest_n(input, n, low, high):
    if(n<1): return ''
    string = input[low:high] if high != 0 else input[low:]
    largest = ''
    for i,c in enumerate(string):
        if c > largest:
            largest = c
            index = i
    
    return largest+str(get_largest_n(input, n-1, index+1+low, -(n-2)))

ans = 0
with open("input.in") as f:
    for line in f:
        output = ""
        line = line.strip()
        
        output += get_largest_n(line, 12, 0, -11)
        print(output)
        ans += int(output)


#### SOL 2 #####
def get_largest_n_1(s, k):
    r = ''
    for skip in range(k-1,-1,-1):
        j=s.index(max(s[:len(s)-skip]))
        r,s = r + s[j],s[j+1:]
    return int(r)

with open("input.in") as f:
    data = f.readlines()

print(sum(get_largest_n_1(s, 2) for s in data))
print(sum(get_largest_n_1(s, 12) for s in data))