class person:
    age=int
    name=str
    def __init__(self,name,age):
     self.name=name
     self.age=age

    def display_person_info(self):
       print(self.name,self.age)


class employee:
    emp_id=int
    salary=int
    def __init__(self,emp_id,salary):
    
     self.emp_id=emp_id
     self.salary=salary

    def display_employee_info(self):
        print(self.emp_id,self.salary) 


class manager(person,employee):
    department:str
    def __init__(self,age,name,emp_id,salary,department):

      person.__init__(self,age,name)
      employee.__init__(self,emp_id,salary)  
      self.department=department
    
    def display_manager_info(self):
     self.display_person_info()
     self.display_employee_info()
     print(self.department) 

manager_instance=manager("paru",22,1,22000,"hr")
manager_instance.display_manager_info()


