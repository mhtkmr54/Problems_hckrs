from sys import argv

script, user_name = argv
prompt = '>$bitches_will_be_bitches$:  '
print "Hi %s , i am %s script" %(user_name, script)
print "I would like to ask a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print "And OS?"
os = raw_input(prompt)


print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r OS.  Nice.
""" % (likes, computer, os)
