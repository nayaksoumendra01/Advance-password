print("welcome to login page...")
print("sign up using mobile number ")

x=input("enter mobile number : ")

while len(x)!=10 or not x.isdigit():
    print("Please enter a valid 10-digit mobile number.")
    x=input("enter mobile number : ")

y=input("password : ")
print("signup successfully...")
print("sign in")

ps=""
at=0 
n=input("Enter your login_id : ")

if n==x:
 logged_in = False
 while at<3:
    ps=input("Enter password : ")
    at+=1

    if ps==y:
        print("..."*10)
        print("login successfully. ")
        print("..."*10)
        print("   ")
        logged_in = True
        break

 if logged_in:
        while True:
        
         print("1. Generate Salary Slip")
         print("2. Change Password")
         print("3. Logout")
         print("   ")

         choice = int(input("Enter your choice: "))
         

         if choice==1 :
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


         elif choice==2:
             old=input("Enter your old password : ")
             if old==y:
                 new=input("Enter your new password : ")
                 renew=input("Enter confirm password : ")
                 if new==renew:
                     print("Password changed successfully...")
                     print("   ")
                     y=new
                 else :
                    print("password not match...")
             else :
                 print("Please Enter Correct Password...")
                 print("   ")  


         elif choice==3:
             print("Logout Program Finished...") 
             break

         else:
             print("Enter correct choice option... ")
          
                           
 else:
            print("Wrong password attempt count is : ",at)
            if at==3:
                 print("Attempt expired")           
                 
else:
    print("Invalid login id")