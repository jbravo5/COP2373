import csv

# Function to create the CSV file and write student data
def create_grades_file():
    # Ask user how many students
    num_students = int(input("Enter number of students: "))

    # Open CSV file in write mode
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop to enter each student
        for i in range(num_students):
            print(f"\nEntering data for student {i+1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write student record
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv file created successfully!\n")


# Function to read and display CSV file in table format
def display_grades_file():
    # Open CSV file in read mode
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\n--- Student Grades ---\n")

        # Print each row in formatted style
        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))


# Main function to call both functions
def main():
    create_grades_file()
    display_grades_file()


# Run the program
main()
