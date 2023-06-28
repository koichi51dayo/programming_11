class data:
    def __init__(self,num,name,profile,next):
        self.num=num
        self.name=name
        self.profile=profile
        self.next=next


       
def make_list():
    p=data(None,None,None,None)
    with open("Zac_Japan.txt",'r', encoding="utf-8") as f:
        a=f.readlines()
        for i in a:
            b=i.split()
            newp=data(int(b[0]),str(b[1]),str(b[2]),next=p)
            p=newp
            
    return p
            
def print_list(p):
    while p.num!=None:
        print("{:>2} {} {}".format(p.num,p.name,p.profile))
        p=p.next
        
            
def search(x:int,p):
        if p.num==None:
            print("該当者はいません\n")
        elif x==p.num:
            print("削除しました\n")
            q=p.next
            p.num,p.name,p.profile,p.next=q.num,q.name,q.profile,q.next
        else:
            search(x,p.next)
        

p=make_list()
while True:
    x=int(input("\n背番号を入力してください(0を入力で終了)："))
    if x==0:
        print("探索を終了します")
        break
    elif p.num==x:
        p=p.next
        print("削除しました\n")
        if p.num==None:
            print("null")
        else:
            print_list(p)
    elif p.num==None:
        print("null")
    else:
        search(x,p.next)
        print_list(p)