ps=""
at=0
n=input("Enter your login_id : ")
if n=="xyz@cutm.ac.in":
 while ps!="cutm" and at<3:
    ps=input("Enter password : ")
    at+=1
    if ps=="cutm":
        print("..."*10)
        print("login successfully. ")
        print("..."*10)
        name=(input("Enter your name : "))
        basic=int(input("Enter your basic salary : "))
        bonus=int(input("Enter Bonus amount : "))
        tax=int(input("enter tax percentage : "))
        
        gross=basic+bonus
        amount=(gross*tax)/100
        net=gross-amount
        print("---"*20)
        print("hello ",name,"below is your salary slip")
        print("---"*20)
        print("Your gross salary is : ",gross)
        print("Your tax amount is : ",amount)
        print("Your net salary amount is : ",net)
        print("---"*20)
        print("thank you")
    else:
            print("Wrong password attempt count is : ",at)
            if at==3:
                 print("Attempt expired")
else:
    print("Invalid login id")
