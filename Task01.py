
tasks_list=[]
def create_list():
    task_name=input("Enter a task: ")
    tasks_list.append(task_name)
    print("==Element in the list added Successfully==")
def delete_task():
    if(len(tasks_list)==0):
        print("No tasks in the list to delete.")
        print("First add tasks in the list to continue the deletion.")
        return
    print("Tasks list are:")
    for index,task in enumerate(tasks_list):
        print(f'At index number "{index}"--->Task is "{task}"')
    ran=int(input("Enter a index number from the above tasks to delete: "))
    for i in range(0,len(tasks_list)):
        if(ran==i):
            del tasks_list[ran]
            print("Task deleted Successfully.")
    if(ran<0):
        print("please enter the value in the range(0-len(tasks_list))") 
def view_tasks():
    if(len(tasks_list)==0):
        print("No tasks in the list to print.")
        print("First add tasks in the list to print.")
    else:
        for index,task in enumerate(tasks_list):
            print(f'At index number "{index}"--->Task is "{task}"')
    print(tasks_list)
print("===Welcome to To-Do List application=====")
def main():   
    while (True):
        print("1. For adding new task in the list enter (1)")
        print("2. For deleting a task from the list enter (2)")
        print("3. For printing the tasks available in the list enter (3)")
        print("4. Quit:")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            create_list()
        elif(choice==2):
            delete_task()
        elif(choice==3):
            view_tasks()
        elif(choice==4):
            print("Thanks for using To-Do list application")
            break
        else:
            print("please enter a valid choice.")
if __name__ == "__main__":
    main()