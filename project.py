import re
class Student():#student class

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = {}

    def set_grade(self,subject,grade):
        if not(subject in self.grades.keys()):
            self.grades[subject] = []
        self.grades[subject].append(str(grade))

    def Average(self):
        summ = 0
        lenght = 0
        for subject in self.grades.keys():
            for grade in self.grades[subject]:
                summ += int(grade)
                lenght += 1
        return str(summ/lenght)

ls = []#students storage
f = open("data.txt", "w")#check existance
f.close()
f = open("data.txt", "r+")
txt = f.read()#read data
for x in txt.split(";")[:-1]:#load data
    st_name = re.search(r"\w+",x).group()
    age = re.search(r"\w+\:(?P<age>\d+)",x).group("age")
    grades = {}
    x = re.search(r"\*.+",x).group()
    x = x[1:]
    subject = x.split("|")[:-1]
    for y in subject:
        name = re.search(r"[a-zA-Z]+",y).group()
        grade = re.findall(r"\d+",y)
        grades[name] = grade
    ls.append(Student(st_name,age))#set data
    ls[-1].grades = grades
def search(nm):#search student in storage
    for x in ls:
        if x.name == nm:
            return x
while True:
    print("1. New Student\n2. Add grade\n3. Remove Student\n4. Average grade\n5. List students\n6. List grades\n7. Exit")
    en = input("Select option: ")
    try:
        if en == "1":
            name = input("Enter student name: ")
            age = input("Enter age: ")
            ls.append(Student(name,age))
            print("Student {} added.".format(name))
        elif en == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            search(name).set_grade(subject,grade)
        elif en == "3":
            name = input("Enter student name: ")
            ls.remove(search(name))
            print("Student removed.")
        elif en == "4":
            name = input("Enter student name: ")
            print("The average grade is {}".format(search(name).Average()))
        elif en == "5":
            for st in ls:
                print("{}, Age:{}".format(st.name,str(st.age)))
        elif en == "6":
            for st in ls:
                print(st.name + ":")
                gr = ""
                for subs in st.grades.keys():
                    for x in st.grades[subs]:
                        gr += x + ", "
                    print("{}: {}".format(subs,gr))
                    gr = ""
                print("\n")
        elif en == "7":
            f.close()
            f = open("data.txt", "w")
            f.truncate()#clear
            txt = ""#save
            for st in ls:
                txt += st.name + ":" + str(st.age) + "*"
                gr = ""
                for sub in st.grades.keys():
                    for x in st.grades[sub]:
                        gr += x + ", "
                    txt += sub + ":" + gr
                    txt += "|"
                txt += ";"
            f.write(txt)#save
            f.close()
            print("Goodbye")
            break#exit()
        except:
            print("Wrong data given")
