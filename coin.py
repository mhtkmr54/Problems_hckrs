# Enter your code here. Read input from STDIN. Print output to STDOUT

a = raw_input()
a = [int(i) for i in a.split(',')]
print a
S = int(raw_input())
print "sssssssssssssssss",S
dp = [0 for i in range(2 * S + 1)]
print "BEFORE DDPPPPPPPPPPPPPPPPPPp",dp
dp[0] = 1
for v in a:
    print "for coin",v
    for i in range(S):
        dp[i + v] += dp[i]
        print "looooooooooooop number in range(s)",i
        print "infirstloop of range(s) ",dp
    print "////////////////////////AFter loop ends////////////////////////",dp

print "------------------------------the end-----------------",dp
print dp[S]

