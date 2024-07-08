import jwt
import sqlite3
conn = sqlite3.connect('to_do_list.db')


cursor=conn.cursor()
def jwt_authentication(name,password):
    header={
        "alg": "HS256",  
        "typ": "JWT" 
    }
    payload={
        "name":name,
        "password":password
    }
    secret="manasa"
    encoded_jwt=jwt.encode(payload, secret, algorithm='HS256', headers=header)  
    print(encoded_jwt)
    sign_up=("insert into auth_db(token,user_name) values (?,?);")
    cursor.execute(sign_up,(encoded_jwt,name,))
    conn.commit()
    decoded_jwt=jwt.decode(encoded_jwt, secret, algorithms=['HS256'])  
    print(decoded_jwt) 
def sign_in(name,password):
    header={
        "alg": "HS256",  
        "typ": "JWT" 
    }
    
    payload={
        "name":name,
        "password":password
    }
    secret="manasa"
    encoded_jwt=jwt.encode(payload, secret, algorithm='HS256', headers=header)  
    print(type(encoded_jwt))
    sign=("select * from auth_db ;" )
    data=cursor.execute(sign)
    flag=0
    for i in data:
        if i[0]==encoded_jwt and i[1]==name:
            flag=1
            break
    
        
    if flag==1:
        t=int(input("if you want to get your task details please press 1"))
        if t==1:
            script=("select * from to_do where user_name=(?);")
            k=cursor.execute(script,(name,))
            for i in k:
                print(i)
        else:
            print("!!!!!---------GOOD BYE-----------!!!!!!")
            exit
    else:
        print("!!!!!------------user has not yet signed up please sign-up---------!!!!!!!")

    



"""table='create table auth_db(token varchar(300),user_name varchar(100), primary key(user_name))'
cursor.execute(table)
"""

 
if __name__ == '__main__':
    while 1:
        print("press\n 1 for sign in \n 2 for sign up")
        k=int(input())
        if k==1:
            name = input("enter your name please:\n ")
            password = input("your password:\n ")
            sign_in(name,password)
            
        
        elif k==2:
            name = input("enter your name please:\n ")
            password = input("your password:\n ")
            jwt_authentication(name,password)

        else:
            print("wrong input please try again\n")
            break

conn.close()