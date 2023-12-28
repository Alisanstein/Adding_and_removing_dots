def add_dots(string):
    lis = list(string)
    count = 1
    for i in range(len(lis)):
        if count == len(lis):
            break
        lis.insert(count,'.')
        count += 2
    output = ''.join(lis)
    return output

def remove_dots(string):
    return (string.replace('.',''))