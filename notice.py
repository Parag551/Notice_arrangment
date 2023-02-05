name = input("Enter your name :")
date = input("Enter date :")
father = input("Enter your fathers name :")
mother = input("Enter your mothers name :")
dob = input("Enter your date of birth :")


Note = '''
Good morning <|name|> ,

   We are glad to inform you that you are selected in our company.

As per your information your details are -

         your fathers name is <|father|> 
         your mothers name is <|mother|>
         Your date of birth is <|dob|> 

 THANK YOU , for your concern
     Have a great day 
       <|date|>
 '''

print(Note.replace('<|name|>', name).replace('<|date|>', date).replace('<|father|>', father).replace('<|mother|>', mother).replace('<|dob|>', dob))