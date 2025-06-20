# look for students by id, compare the id entered by the user , implement number's validation with available id's in student list.


students = [
    {"name": "henry",
     "id": 0, 
     "age": 18, 
     "notes" : [7, 3, 5]},
    {"name": "john", 
     "id": 1, 
     "age": 15, 
     "notes" : [6, 3, 7]},
    {"name": "samuel", 
     "id": 2, 
     "age": 16, 
     "notes" : [9, 4, 8]}
]

# this function handles the info that is introduced in the main list
def register_student():
    name = input("enter your name: ")
    try:
        age = int(input("enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return
    worth_id = (students[-1]["id"] )
    worth_id += 1


    notes = []
    for i in range(3):
        try:
            note = float(input(f"enter the note {i+1}:"))
            notes.append(note)
        except ValueError:
            print("Invalid note. Try again.")
            return

    add_students = {"name": name, "id": worth_id,"age": age, "notes": []}

    add_students["notes"] = notes
    students.append(add_students)

    return add_students

#this function consult the info of a student in the list
def consult_student():
    try:
        consult_id = int(input("enter your id: "))
    except ValueError:
        print("Invalid ID. must be a number")
        return

    found = False

    for student in students:
        if student["id"] == consult_id:
            print(f"Name: {student['name']}, age: {student['age']}, notes: {student['notes']}")
            print(f"Average: {sum(student['notes']) / len(student['notes'])}")
            found = True
            break
    if not found:
        print("Student not found.")

    return

#This function update the note of a student of the list
def update_notes():
    try:
        get_id = int(input("enter your ID: "))
    except ValueError:
        print("Invalid ID. must be a number.")
        return

    found_data = False

    for student in students:
        if student["id"] == get_id:
            new_notes = []
            for i in range(3):
                try:
                    note = float(input(f"Enter new note {i+1}: "))
                    new_notes.append(note)
                except ValueError:
                    print("Invalid note. try again")
                    return

            student["notes"] = new_notes
            print("Notes updated sucessfully.")
            found_data = True
            break

    if not found_data:
        print("student not found.")

        return
        
#this function delete a student of the list with all his information.
def delete_students():
    try:
        number_id = int(input("enter your ID: "))
    except ValueError:
        print("Invalid ID. must be a number.")
        return

    found_delete = False

    for i in range(len(students)):
        if students[i]["id"] == number_id:
            students.pop(i)
            print("student deleted succesfully.")
            found_delete = True
            break
    if not found_delete:
        print("Student not found.")

        return

#the main menu of the program
election = 0
while election != 6:

    print("choose between one of the six options")
    print("1. register to student")
    print("2. consult to student")
    print("3. update notes")
    print("4. delete student")
    print("5. see all students")
    print("6. exit")
    try:
        election = int(input("enter a number from 1 to 6: "))
    except ValueError:
        print("invalid input. Please enter a number.")
        continue
    if election == 1:
        print(register_student())
    elif election == 2:
        print(consult_student())
    elif election == 3:
        print(update_notes())
    elif election == 4:
        print(delete_students())
    elif election == 5:
        print(students)
    elif election == 6:
        print("exiting the program...")
    else:
        print("invalid option. try again.")