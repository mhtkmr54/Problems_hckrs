import sys,re
p = []



def check_para(coords):
   for i in  coords:
     z = map(int,i)
     p.append(z)
     print p
   count = 0 
   ac = [p[2][0]-p[0][0],p[2][1]-p[0][1]]
   bd = [p[3][0]-p[1][0],p[3][1]-p[1][1]]
   db =  map(lambda x: x * -1, bd)
   ab = [p[1][0]-p[0][0],p[1][1]-p[0][1]]
   cd = [p[3][0]-p[2][0],p[3][1]-p[2][1]]
   ad = [p[3][0]-p[0][0],p[3][1]-p[0][1]]
   bc = [p[2][0]-p[1][0],p[2][1]-p[1][1]]
   cb =  map(lambda x: x * -1, bc)


   if ac == bd and ab == cd:
        print "parallelogram exists as given"
        print p[0],p[2],p[3],p[1]
   
   elif  ac == db and ad == cb:
        print "parallelogram exists as given"
        print p[0],p[2],p[1],p[3]
   
   elif ad == bc and ab == dc:
        print "parallelogram exists as given"
        print p[0],p[3],p[2],p[1]

        
   else:
        print "no parallelogram exists"





def main():
    tc=raw_input(">>")
    r = re.compile(r"([0-9,]+[0-9])+")
    coord = re.findall(r,tc)
    coords = []
    for i in coord:
         print i
         coords.append(i.split(","))
    print coords
    check_para(coords)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
