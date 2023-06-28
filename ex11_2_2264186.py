class data:
    def __init__(self,num,name,profile,next):
        self.num=num
        self.name=name
        self.profile=profile
        self.next=next

p=None
       
def make_list():
    global p
    with open("Zac_Japan.txt",'r', encoding="utf-8") as f:
        a=f.readlines()
        for i in a:
            b=i.split()
            newp=data(int(b[0]),str(b[1]),str(b[2]),next=p)
            p=newp
            
def search(x:int,p:list):
    while True:
        if p==None:
            print("該当者はいません\n")
            break
        elif x==p.num:
            print("{:>2} {} {}\n".format(p.num,p.name,p.profile))
            break
        p=p.next
        
