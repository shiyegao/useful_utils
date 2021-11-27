class a:
    def b(self, s):
        print(s)
    
    def c(self, s):
        getattr(self, 'b')(s)
    

A = a()
A.c('haha') 