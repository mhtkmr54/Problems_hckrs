import sys,re
tc=int(raw_input())
r=re.compile(r"[a-zA-Z_.-0-9+]+@[a-zA-Z0-9.]+[a-zA-Z]+")
emailIds=[]
lines=[]
for _ in range(tc):
    line=sys.stdin.readline().strip()
    lines.append(line)

print lines

for line in lines:
    emails=re.findall(r,line)
    for email in emails:
        emailIds.append(email.strip())
emailIds=list(set(emailIds))
s=''
for e in sorted(emailIds):
    s+=e+';'
print s[:-1]
