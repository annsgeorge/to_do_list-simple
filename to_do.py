tasks=[]

def addtask():
  task=input("Enter your task:")
  tasks.append(task)
  print("Tasks:")
  print(task)


def listtask():
  print("Task List:")
  if not tasks:
    print("No current tasks!!!")
    
  else:
    for index,task in enumerate(tasks):
       print(f"{index}:{task}")
  
def deletetask():
  listtask()
  try:
    todelete=int(input())
    if todelete>=0 and todelete <len(tasks):
      tasks.pop(todelete)
      print("Enter index of task to delete")
      print(f"Task {todelete} has been removed")
    else:
      print("Invalid")

  except:
    print("Invalid")
   

if __name__ =="__main__":
  print("TO DO LIST")
  while True:
    print("Menu:")
    print("1.Add")
    print("2.Delete")
    print("3.List")
    print("4.Exit")

    choice = input("Enter your choice:")


    if(choice =="1"):
      addtask()
    elif(choice =="2"):
      deletetask()
    elif(choice =="3"):
      listtask()
    elif(choice =="4"):
      break
    else:
      print("Error!")

