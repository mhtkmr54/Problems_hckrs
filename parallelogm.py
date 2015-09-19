import sys,re
p = []

def check_para(coords):
   for i in  coords:
     z = map(int,i)
     p.append(z)
   count = 0 
   ac = [p[2][0]-p[0][0],p[2][1]-p[0][1]]
   bd = [p[3][0]-p[1][0],p[3][1]-p[1][1]]
   db =  map(lambda x: x * -1, bd)
   ab = [p[1][0]-p[0][0],p[1][1]-p[0][1]]
   cd = [p[3][0]-p[2][0],p[3][1]-p[2][1]]
   ad = [p[3][0]-p[0][0],p[3][1]-p[0][1]]
   bc = [p[2][0]-p[1][0],p[2][1]-p[1][1]]
   cb =  map(lambda x: x * -1, bc)

  # 3 cases if parallelogram can be picked up out of the plane and turned over

   if ac == bd and ab == cd:
        print "parallelogram exists as given"
        print "seen clockwise from first coordinate ",p[0],p[1],p[3],p[2]
        print "seen anti-clockwise from first coordinate ",p[0],p[2],p[3],p[1]
   
   elif  ac == db and ad == cb:
        print "parallelogram exists as given"
        print "seen clockwise from first coordinate ",p[0],p[2],p[1],p[3]
        print "seen anti-clockwise from first coordinate ",p[0],p[3],p[1],p[2]

   
   elif ad == bc and ab == dc:
        print "parallelogram exists as given"
        print "seen clockwise from first coordinate ",p[0],p[3],p[2],p[1]
        print "seen anti-clockwise from first coordinate ",p[0],p[1],p[2],p[3]

        
   else:
        print "The coordinates do not form the vertices of a parallelogram"





def main():
    print "your input format -- (0,0), (0,1), (1,0), (1,1)"
    tc=raw_input(">>")
    r = re.compile(r"([0-9,]+[0-9])+")
    coord = re.findall(r,tc)
    coords = []
    for i in coord:
         coords.append(i.split(","))
    check_para(coords)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
