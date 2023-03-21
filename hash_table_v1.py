class hash_table(list):
    def __init__(self,list):
        self.m = 2*len(list)
        self.l= self.m*[None]
        
    def hash_function(self, x):
        print(self.l)
        return x%self.m

if __name__== "__main__":
    print("hola")
    #ht =hash_table([1,2,3,4])
    #print(type(ht.l))