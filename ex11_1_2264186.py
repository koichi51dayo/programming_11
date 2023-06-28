class data:
    def __init__(self,num,name,profile,next):
        self.num=num
        self.name=name
        self.profile=profile
        self.next=next
        
def print_list(p):
    while p!=None:
        print("{:>2} {} {}".format(p.num,p.name,p.profile))
        p=p.next
        
with open("Zac_Japan.txt",'r', encoding="utf-8") as f:
    a=f.readlines()
    p=None
    for i in a:
        b=i.split()
        newp=data(int(b[0]),str(b[1]),str(b[2]),next=p)
        p=newp
        
print_list(p)
        

   
        