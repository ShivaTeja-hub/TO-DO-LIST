import sqlite3

conn = sqlite3.connect('to_do_list.db')

cursor=conn.cursor()


class task:
    def __init__(self,name,description,priority,status,user_name):
        self.name=name
        self.description=description
        self.priority=priority
        self.status=status
        self.user_name=user_name
    def display(self):
        print(self.name)
        print(self.description)
        print(self.status)
        print(self.user_name)
print("welcome to to do app/n")
def add_task(priority,task_name,description,user_name):
    script=("insert into to_do (task_name,description,priority,status,user_name  ) values (?,?,?,?,?);")
    cursor.execute(script,(task_name,description,priority,'To-be-done',user_name))
    

def view_task():
    data=cursor.execute('select * from to_do')
    for i in data:
        print(i)
    
def task_status(name):
    script=("select * from to_do where task_name=(?);")
    output=cursor.execute(script,(name,))
    for i in output:
        print(i)
def update_task(name,k):
    script=("update to_do set status=(?) where task_name=(?);")
    cursor.execute(script,(k,name))
    print("your task updating is done")
    
def delete_task(remove):
    script=("delete from to_do where task_name=(?);")
    cursor.execute(script,(remove,))
    print("#######task you deleted is############ ")
    print(script)

"""table='create table to_do(task_name varchar(100),description varchar(200),priority int,status varchar(100),user_name varchar(100), foreign key(user_name) references auth_db(user_name) )'

cursor.execute(table)
"""


task_list=[]
while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. status of task")
        print("4. Update Task Details")
        print("5. Delete Task")
        print("6. Exit")
        choice=int(input("please select your choice from above list\n"))
        if choice==1:
            task_name=input("please enter your task name\n")
            description=input("please enter the description of the task\n")
            priority=int(input("please give the priority of task \n"))
            name=input("please enter your user name")
            task_list=add_task(priority,task_name,description,name)
        if choice==2:
            print("the tasks you have are\n")
            view_task()
        if choice==3:
            task_name=input("please enter your task name to know the status:\n")
            task_status(task_name)

        if choice==4:
            name=input("please enter the task name to update:\n")
            stat=int(input("please enter 1 for completed \n 2 for  in-progress \n 3 for to-be-done-later"))
            if stat==1:
                k='completed'
                delete_task(name)
            elif stat==2:
                k='inprogress'
            elif stat==3:
                k='to-be-completed'
            else:
                exit

            update_task(name,k)
        if choice==5:
            remove=input("enter the name of task you want to delete:\n")
            delete_task(remove)

        if choice==6:
            print("!!!!!--------------------BYEEEEEEEEEE-----------------!!!!!\n")
            break
        
conn.commit()
conn.close()