#imports

from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import DeclarativeBase,sessionmaker,relationship
from sqlalchemy.exc import IntegrityError


#Creating the database 

class Base(DeclarativeBase):
    pass

engine=create_engine("mysql+pymysql://root:root@localhost:3306/tasks")
Session=sessionmaker(bind=engine)
session=Session()

#Creating Models

class Users(Base):

    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name =Column(String(50), nullable=False)
    email=Column(String(50),nullable=False,unique=True)
    tasks=relationship("Task",back_populates="user",cascade="all , delete-orphan")

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True)
    title=Column(String(50),nullable=False,unique=True)
    description=Column(String(50))
    user_id=Column(Integer,ForeignKey("users.id"))
    user=relationship("Users",back_populates='tasks')


Base.metadata.create_all(engine)


#Utility function 

def get_user_by_email(email):
    return session.query(Users).filter_by(email=email).first()
def confirm_action(promt:str)-> bool:
    return input(f"{promt} (yes/no) ").strip().lower()=='yes'

# CRUD operations

def add_user():
    name,email=input("Enter the username: "),input("Enter the email: ")
    if get_user_by_email(email):
        print(f"User already exists:  {email}") 
        return
    try:
        session.add(Users(name=name,email=email))
        session.commit()
        print(f"User :{name} added!")
    except IntegrityError as e:
        session.rollback()
        print(f"ERROR: {e}")

def add_task():
    email=input("Enter the email of the user to add tasks: ")
    user=get_user_by_email(email)
    if not user:
        print(f"No user found with that email!")
        return
    title,description=input("Enter the title : "),input("Enter the description: ")
    session.add(Task(title=title,description=description,user=user))
    session.commit()
    print(f"Added tot the database : {title}:{description}")


# Query 

def query_users():
    for user in session.query(Users).all():
        print(f'ID {user.id},Name:{user.name},Email:{user.email}')

def query_task():
    email=input("Enter the email of the user for the task: ")
    user=session.query(Users).filter_by(email=email).first()
    if not user:
        print("There was no user with this email: ")
        return 

    for task in user.tasks:
        print(f'Task ID:{task.id},Title: {task.title},Description:{task.description}')
        return
    print("No tasks")

def update_user():
    email=input("Email of ho you what to update: ")
    user=get_user_by_email(email)
    if not user:
        print("There is no user with that email")
        return
    user.name=input("Enter a new name for the user(leave blank to stay the same): ") or user.name
    user.email=input("Enter a new email for the user(leave blank to stay the same): ") or user.email
    session.commit()
    print("User updated!")

def delete_user():
    email=input("Enter the email of the user you want to delete: ")
    user=get_user_by_email(email)
    if not user:
        print("There is no user with that email")
        return
    if confirm_action(f"Are you sure you want to delete the user: {user.name}?"):
        session.delete(user)
        session.commit()
        print("User deleted succeessfully!")

def delete_task():
     email=input("Enter the email linked to the tasks : ")
     user= get_user_by_email(email)

     for task in user.tasks:
         print(f"Task ID: {task.id},Title: {task.title} ")
     task_Id=input("Enter the ID of the task  you want to delete: ")
     task=next((t for t in user.tasks if str(t.id)== task_Id),None)
     if confirm_action(f"Are you sure you want to delete the user: {task_Id}?"):
            session.delete(task)
            session.commit()
            print("Task deleted succeessfully!")
# Main ops

def main()->None :
    actions={
        "1":add_user,
        "2":add_task,
        "3":query_users,
        "4":query_task,
        "5":update_user,
        "6":delete_user,
        "7":delete_task
    }
    while(True):
         print("\nOptions:\n1. Add Users\n2. Add Task\n3. Query Users\n4. Query Task\n5. Update User\n6. Delete User\n7. Delete Task\n8. Exit")
         choice=input("Enter an option: ")
         if choice=="8":
             print("Adios")
             break
         action=actions.get(choice)
         if action:
             action()
         else:
             print("That is not an option!")

if __name__=="__main__":
    main()