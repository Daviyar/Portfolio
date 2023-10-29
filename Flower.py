#DJ Goddard 10/29/23 Code States whether the flowers listed are blooming or growing
class Flower:#stating the class (attributes)
    def __init__(self, name): #assigning value to "name"
        self.name = name

    def grow(self):#defining class of grow
        print("The " +self.name + " is growing.")#states that the flower is growing

    def bloom(self):#defining class of bloom
        print("The " + self.name + " is blooming.")#states that the flower is blooming

def main():#defining (methods)
    flower1 = Flower("Rose")#identifying flower1 as a Rose
    flower1.grow()#calls grow for flower1
    flower1.bloom()#calls bloom for flower 1
    flower2 = Flower("Daisy")#identifies flower2 as a Daisy
    flower2.grow()#calls grow for flower2
    flower2.bloom()#calls bloom for flower 2

if __name__ == "__main__":#checks if script is being run directly
  main()