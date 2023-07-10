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
            
def print_list(p):
    while p!=None:
        print("{:>2} {} {}".format(p.num,p.name,p.profile))
        p=p.next
            
def print_list(p):
    while p!=None:
        print("{:>2} {} {}".format(p.num,p.name,p.profile))
        p=p.next
    

def merge_sort(head):
    if head.next==None or head==None:
        return head
    
    middle=get_middle(head)
    nextmiddle=middle.next
    middle.next=None
    
    left=merge_sort(head)
    right=merge_sort(nextmiddle)
    head=merge(left,right)
    
    return head
    
def get_middle(head):
    slow=head
    fast=head
    
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        
    return slow

def merge(left,right):
    if left is None:
        return right
    if right is None:
        return left

    if left.num < right.num:
        merged = left
        merged.next = merge(left.next, right)
    else:
        merged = right
        merged.next = merge(left, right.next)
    
    return merged

make_list()
ans=merge_sort(p)
print_list(ans)
        