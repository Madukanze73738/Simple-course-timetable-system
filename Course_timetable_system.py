timetable = []

def add_schedule():
    course = input("Enter course name: ")
    day = input("Enter day: ")
    time = input("Enter time: ")
    timetable.append({"course": course, "day": day, "time": time})
    print("Schedule added")

def view_timetable():
    if not timetable:
        print("No timetable available")
    else:
        for item in timetable:
            print(item["course"], "-", item["day"], "-", item["time"])

def main():
    while True:
        print("1. Add Schedule")
        print("2. View Timetable")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_schedule()
        elif choice == "2":
            view_timetable()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
