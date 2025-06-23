# student_system.py

students = []

def add_student():
    name = input("Enter name: ")
    student_id = input("Enter student ID: ")
    scores = []
    for i in range(3):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)
    total = sum(scores)
    students.append({
        "name": name,
        "id": student_id,
        "scores": scores,
        "total": total
    })
    print("Student added.\n")

def show_all_students():
    if not students:
        print("No students yet.")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"{s['name']} | ID: {s['id']} | Scores: {s['scores']} | Total: {s['total']}")
    print()

def show_top_3():
    if len(students) < 3:
        print("Not enough students to show top 3.")
        return
    sorted_list = sorted(students, key=lambda x: x['total'], reverse=True)
    print("\n--- Top 3 Students ---")
    for i, s in enumerate(sorted_list[:3]):
        print(f"{i+1}) {s['name']} - Total: {s['total']}")
    print()

def find_by_id():
    search_id = input("Enter student ID to search: ")
    for s in students:
        if s['id'] == search_id:
            print(f"Found: {s['name']} | Scores: {s['scores']}")
            return
    print("Student not found.")

def save_to_file():
    with open("students.txt", "w") as file:
        for s in students:
            line = f"{s['name']},{s['id']},{','.join(map(str, s['scores']))},{s['total']}\n"
            file.write(line)
    print(" Data saved to students.txt\n")

def load_from_file():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 6:
                    name = parts[0]
                    student_id = parts[1]
                    scores = list(map(float, parts[2:5]))
                    total = float(parts[5])
                    students.append({
                        "name": name,
                        "id": student_id,
                        "scores": scores,
                        "total": total
                    })
        print(" Data loaded from students.txt\n")
    except FileNotFoundError:
        print(" No saved data found. Starting fresh.\n")


def main():
    load_from_file()  

    while True:
        print("======== Student Record System =======")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Show Top 3 Students")
        print("4. Search by ID")
        print("5. Save to File")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            show_top_3()
        elif choice == "4":
            find_by_id()
        elif choice == "5":
            save_to_file()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
