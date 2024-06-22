print("                                                         Welcome to the Quiz","\n")

def Sel_Role():
    print("                                                     Quiz Master   ->   Press 1")
    print("                                                     Quiz Cracker  ->   Press 2")  

#Sel_Role()
Question={}
Question_1=[]
def Quiz():
    while True:
        Sel_Role()
        Sel_Option=int(input("Select Your Role: "))
        if Sel_Option==1:
            print("                                             Welcome to MASTER")
            print("                                             SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUIESTIONS.....")


            print("                                             Press 1  -       Add Your Question: ")
            print("                                             Press 2  -       View Questions: ")
            print("                                             Press 3  -       Delete questions")
            print("                                             Press 4  -       Exit")

            Sel_Option_2=int(input("Select Master Quiz Options: "))
            if Sel_Option_2==1:
                #Add_Question={}
                Que_Num=int(input("Enter Number Of Question: "))
                for i in range(Que_Num):
                                       
                  
                    Que=input("Enter a Question: ")
                    Ans=input("Enter a Answer: ")
                    option_1=input("Enter Option 1: ")
                    option_2=input("Enter Option 2: ")
                    
                    Question["Question ":Que]={"Op_1":option_1,"Op_2":option_2,"Ans":Ans}
                    List=list(Question.items())


                    #Question["Question",Que]={"Op_1":option_1,"Op_2":option_2,"Ans":Ans}
                    continue
               
            elif Sel_Option_2==2:
                if len(Question) >0:
                    #print(Question_1)
                    print(List)
                else:
                    print("No Data Found...")
                 
                continue

            elif Sel_Option_2==3:
                                    
                Delete=input("Enter Question Number: ")

                if Delete in Question:
                    D=List.pop(Question)
                    print(f"Delete'{Delete}' Question.")
                else:
                    print(Delete,"No..  Question Found In Question..")
                    print(List)

                

                
            elif Sel_Option_2==4:
                print("Exit The Game:")
                break
        elif Sel_Option==2:
            
                if len(Question) >0:
                    print("Question: ",Que)
                    print("Option_1: ",option_1)
                    print("Option_2: ",option_2)

                    answer=input("Enter Your Answer: ")

                    if answer==Ans:
                        print("your Answer is Correct...","\n")
                    elif answer != Ans:
                        print("Answer is Wrong...")
                        print("Correct Answer is: ",Ans)
                    else:
                        print("Pleace Enter Vaild Answer!","\n")
                else:
                    print("No... Quiz Data Found....")
                    
        else:
            print(" No Option Not Found...","\n","Pleace Select Valid Option")
Quiz()            








