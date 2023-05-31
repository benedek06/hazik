class Q:
    def __init__(self):
        self.head=None

    def insertion(self,nev,data):
        newnode=N(data,nev)
        
        
        if self.head==None:
            self.head=newnode
            return
        
        else:
            if(self.head.data<=data):
                temp=self.head
                self.head=newnode
                self.head.next=temp
                return
        
        if self.head==None:
            self.head=newnode
            return
        else: 
            n=self.head
            while(n.next!=None or n.data<=data):
                if(n.data<=data):
                    temp=n
                    n=newnode
                    n.next=temp
                    break
                else:
                    n=n.next
        
            n.next=newnode
    

    def kiir(self):
        if self.head==None:
            return
        else:
            n=self.head
            while(n!=None):
                print(f"{n.nev} {n.data} pontot ért el")
                n=n.next

class N:
    def __init__(self,data,nev):
        self.nev=nev
        self.data=data
        self.next=None


root=Q()
root.insertion("Bálint",5)
root.insertion('Marci',15)
root.insertion("Boti",19)
root.insertion("Kristóf",11)
root.kiir()