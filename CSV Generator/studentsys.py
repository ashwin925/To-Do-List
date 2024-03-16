import csv
import random
import string
import tkinter as tk
from tkinter import messagebox

class StudentGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Data Generator")
        
        # Label and entry for number of students
        tk.Label(self.master, text="Number of Students:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.num_students_entry = tk.Entry(self.master)
        self.num_students_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Generate and search buttons
        self.generate_button = tk.Button(self.master, text="Generate Data", command=self.generate_data)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        self.search_button = tk.Button(self.master, text="Search by Reg. No.", command=self.search_student)
        self.search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        
        # Registration number entry for search
        tk.Label(self.master, text="Registration Number:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.reg_no_entry = tk.Entry(self.master)
        self.reg_no_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        # Text area for displaying search result
        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def generate_student_data(self, num_students):
        data = []
        for i in range(1, num_students + 1):
            student = {
                'S.No': i,
                'Name': self.generate_name(),
                'Roll No': self.generate_roll_number(),
                'Reg No': self.generate_reg_number(),
                'Department': self.generate_department(),
                'Course': self.generate_course(),
                'Address': self.generate_address(),
                'College': self.generate_college(),
                'Mobile No': self.generate_mobile_number(),
                'CGPA': self.generate_cgpa()
            }
            data.append(student)
        return data

    def generate_name(self):
        first_names = ['John', 'Emma', 'Michael', 'Sophia', 'Matthew', 'Olivia', 'William', 'Ava', 'James', 'Isabella']
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
        return random.choice(first_names) + ' ' + random.choice(last_names)

    def generate_roll_number(self):
        return ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))

    def generate_reg_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def generate_department(self):
        departments = ['Computer Science and engineering']
        return random.choice(departments)

    def generate_course(self):
        courses = ['B.E']
        return random.choice(courses)

    def generate_address(self):
        cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
        return str(random.randint(100, 999)) + ' ' + random.choice(cities) + ', ' + random.choice(['CA', 'NY', 'TX', 'IL', 'PA'])

    def generate_college(self):
        colleges = ['Anna University']
        return random.choice(colleges)

    def generate_mobile_number(self):
        return ''.join(random.choices(string.digits, k=10))

    def generate_cgpa(self):
        return round(random.uniform(2.0, 4.0), 2)

    def generate_data(self):
        try:
            num_students = int(self.num_students_entry.get())
            student_data = self.generate_student_data(num_students)
            filename = 'studentscsv.csv'
            self.write_to_csv(filename, student_data)
            messagebox.showinfo("Success", f"Generated {num_students} student records successfully and saved to {filename}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of students.")

    def write_to_csv(self, filename, data):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['S.No', 'Name', 'Roll No', 'Reg No', 'Department', 'Course', 'Address', 'College', 'Mobile No', 'CGPA']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in data:
                writer.writerow(student)

    def search_student(self):
        reg_no = self.reg_no_entry.get()
        if reg_no:
            student = self.search_student_by_reg_no('studentscsv.csv', reg_no)
            if student:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "Student found:\n")
                self.result_text.insert(tk.END, f"Name: {student['Name']}\n")
                self.result_text.insert(tk.END, f"Roll No: {student['Roll No']}\n")
                self.result_text.insert(tk.END, f"Reg No: {student['Reg No']}\n")
                self.result_text.insert(tk.END, f"Department: {student['Department']}\n")
                self.result_text.insert(tk.END, f"Course: {student['Course']}\n")
                self.result_text.insert(tk.END, f"Address: {student['Address']}\n")
                self.result_text.insert(tk.END, f"College: {student['College']}\n")
                self.result_text.insert(tk.END, f"Mobile No: {student['Mobile No']}\n")
                self.result_text.insert(tk.END, f"CGPA: {student['CGPA']}\n")
            else:
                messagebox.showinfo("Student Not Found", f"Student with registration number '{reg_no}' not found.")
        else:
            messagebox.showerror("Error", "Please enter a registration number.")

    def search_student_by_reg_no(self, filename, reg_no):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Reg No'] == reg_no:
                    return row
            return None

def main():
    root = tk.Tk()
    app = StudentGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
