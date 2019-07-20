class Matrix:
    def __init__(self,m,n):
        self.M=m
        self.N=n
        self.matrix_=self.crt(m,n)
        
    def crt(self,m,n):
        return [[v for v in range(n)]for i in range(m)]
        # m là hang n la cot
    @property 
    def M(self):
        return self.__m
    @M.setter
    def M(self,v):
        if v<=0:
            print("so hang phai lon hon 0")
            exit()
        else:
            self.__m=v
    @property
    def N(self):
        return self.__n
    @N.setter
    def N(self,v):
        if v<=0:
            print("so cot phai lon 0")
            exit()
        else:
            self.__n=v



    def nhap_matrix(self):
        for v in range(self.__m):
            for i in range(self.__n):
                self.matrix_[v][i]=int(input("matrix["+str(v)+","+str(i)+"]= "))

    def cong(self,matrix_n):
        if matrix_n.M!=self.M or self.N!=matrix_n.N:
            print("không cộng được 2 ma trận khác độ dài")
            exit()
        else:
            res=self.crt(self.__m,self.__n)
            for v in range(self.__m):
                for i in range(self.__n):
                    res[v][i]=self.matrix_[v][i]+matrix_n.matrix_[v][i]
            print(res)
            return res

    def tru(self,matrix_n):
        if matrix_n.M!=self.M or self.N!=matrix_n.N:
            print("không trừ được 2 ma trận khác độ dài")
            exit()
        else:
            res=self.crt(self.__m,self.__n)
            for v in range(self.__m):
                for i in range(self.__n):
                    res[v][i]=self.matrix_[v][i]-matrix_n.matrix_[v][i]
            print(res)
            return res
    def nhan(self,matrix_n):
        if matrix_n.M!=self.M or self.N!=matrix_n.N:
            print("không cộng được 2 ma trận khác độ dài")
            exit()
        else:
            res=self.crt(self.__m,self.__n)
            for v in range(self.__m):
                for i in range(self.__n):
                    res[v][i]=self.matrix_[v][i]*matrix_n.matrix_[v][i]
            print(res)
            return res              
    def chia(self,matrix_n):
        if matrix_n.M!=self.M or self.N!=matrix_n.N:
            print("không cộng được 2 ma trận khác độ dài")
            exit()
        else:
            res=self.crt(self.__m,self.__n)
            for v in range(self.__m):
                for i in range(self.__n):
                    res[v][i]=self.matrix_[v][i]/matrix_n.matrix_[v][i]
            print(res)
            return res





 

x=Matrix(3,2)
x.nhap_matrix()
y=Matrix(3,2)
y.nhap_matrix()
x.cong(y)
x.tru(y)
x.nhan(y)
x.chia(y)



# m=int(input("nhap  chieu dai "))
# n=int(input("nhap chieu rong "))