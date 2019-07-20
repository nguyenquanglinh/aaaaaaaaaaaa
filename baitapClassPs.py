class PhanSo:
    def __init__(self,tu_so,mau_so):
        self.tu=tu_so
        self.mau=mau_so
    
    def __str__(self):
        return str(self.tu)+"/"+str(self.mau)


    @property
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self,m):
        if m==0:
            print("mau so cua 1 phân sô phai khác không")
            exit()
        else:
            self.__mau=m

    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self,v):
        if v==0:
            print("tử số của 1 phân số phải khác không")
            exit()
        else:
            self.__tu=v

    def Cong(self,ps):
        mau=self.mau*ps.mau
        tu=self.tu*ps.mau+self.mau*ps.tu
        #tu=tu*mau+mau*tu
        #mau =mau*mau

        print("kq phep + = ",tu/mau)
        return PhanSo(tu,mau)
    def Tru(self,ps):
        mau=self.mau*ps.mau
        tu=self.tu*ps.mau-self.mau*ps.tu
        #tu=-

        print("kq phep - = ",tu/mau)
        return PhanSo(tu,mau)
    def Nhan(self,ps):
        mau=self.mau*ps.mau
        tu=self.tu*ps.tu
        #tu=tu*tu
        #mau=mau*mau

        print("kq phep * =",tu/mau)
    def Chia(self,ps):
        mau=self.mau*ps.tu
        tu=self.tu*ps.mau
        #tu=tu*mau

        print("kq phep - = ",tu/mau)
        return PhanSo(tu,mau)
    
x=PhanSo(1,3)
y=PhanSo(1,2)
x.Cong(y)
x.Tru(y)
x.Nhan(y)
x.Chia(y)

