class tables:
    def tables(self, nvalue):
        for x in range(2, nvalue+1):
            print("Table of",x,"is:")
            for y in range(1,11):
                print(x,"x",y,"=",x*y)

nvalue=int(input("Enter a value = "))
f = tables()
f.tables(nvalue)