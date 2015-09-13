import fileinput

line = fileinput.input()
n = int(line[0])
for i in range(n):
    s = line[i+1].strip()
    print "ssssssssssssss",s
    for c in s:
      print "cccccc",c
      print "oooordCCC",ord(c)

    lst = [ord(c) for c in s]
    nlst = lst[:]
    nlst.reverse()
    
    ln = len(s)
    funny = True
    for k in range(1, ln):
        if abs(lst[k]-lst[k-1]) != abs(nlst[k]-nlst[k-1]):
            funny = False
            break
            
    if funny: print "Funny"
    else: print "Not Funny"
