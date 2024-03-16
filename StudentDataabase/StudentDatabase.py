import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import csv

class StudentSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Search By Hariom")
        
        self.style = ThemedStyle(self.root)
        self.style.theme_use('equilux')  # Using Equilux theme from ttkthemes
        
        self.create_search_frame()
        self.create_results_frame()
        
    def create_search_frame(self):
        self.search_frame = ttk.Frame(self.root, padding="20")
        self.search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.search_frame, text="Registration Number:").grid(row=0, column=0, sticky=tk.W)
        self.reg_entry = ttk.Entry(self.search_frame, width=20)
        self.reg_entry.grid(row=0, column=1)
        
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_student)
        self.search_button.grid(row=0, column=2)
        
        ttk.Label(self.search_frame, text="Roll Number:").grid(row=1, column=0, sticky=tk.W)
        self.roll_entry = ttk.Entry(self.search_frame, width=20)
        self.roll_entry.grid(row=1, column=1)
        
        self.add_button = ttk.Button(self.search_frame, text="Add/Update", command=self.add_update_student)
        self.add_button.grid(row=1, column=2)
        
    def create_results_frame(self):
        self.results_frame = ttk.Frame(self.root, padding="20")
        self.results_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.results_text = tk.Text(self.results_frame, height=10, width=80)
        self.results_text.grid(row=0, column=0)
        
    def search_student(self):
        reg_no = self.reg_entry.get()
        student = self.find_student(reg_no)
        
        if student:
            self.display_student_info(student)
        else:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Student not found.")
        
    def find_student(self, reg_no):
        with open('students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Reg No'] == reg_no:
                    return row
        return None
    
    def add_update_student(self):
        roll_no = self.roll_entry.get()
        student = self.find_student_by_roll(roll_no)
        if student:
            self.update_student(roll_no)
        else:
            self.add_student()
        
    def find_student_by_roll(self, roll_no):
        with open('students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Roll No'] == roll_no:
                    return row
        return None
    
    def add_student(self):
        with open('students.csv', 'a', newline='') as csvfile:
            fieldnames = ['S.No', 'Name', 'Roll No', 'Reg No', 'Department', 'Course', 'Address', 'College', 'Mobile No', 'CGPA']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            name = input("Enter name: ")
            roll_no = input("Enter roll number: ")
            reg_no = input("Enter registration number: ")
            department = input("Enter department: ")
            course = input("Enter course: ")
            address = input("Enter address: ")
            college = input("Enter college: ")
            mobile_no = input("Enter mobile number: ")
            cgpa = input("Enter CGPA: ")
            
            writer.writerow({
                'S.No': '',
                'Name': name,
                'Roll No': roll_no,
                'Reg No': reg_no,
                'Department': department,
                'Course': course,
                'Address': address,
                'College': college,
                'Mobile No': mobile_no,
                'CGPA': cgpa
            })
            messagebox.showinfo("Success", "Student added successfully!")
        
    def update_student(self, roll_no):
        # Assuming you want to update CGPA only for demonstration
        cgpa = input("Enter new CGPA: ")
        Course = input("Enter new course: ")
        Mobile = input("Enter new mobile no: ")
        Address = input("Enter new Adress: ")
        with open('students.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
        with open('students.csv', 'w', newline='') as csvfile:
            fieldnames = ['S.No', 'Name', 'Roll No', 'Reg No', 'Department', 'Course', 'Address', 'College', 'Mobile No', 'CGPA']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in rows:
                if row['Roll No'] == roll_no:
                    row['CGPA'] = cgpa
                    row['Course'] = Course
                    row['Mobile No'] = Mobile
                    row['Address'] = Address
                writer.writerow(row)
            messagebox.showinfo("Success", "Student details updated successfully!")

    def display_student_info(self, student):
        self.results_text.delete(1.0, tk.END)
        info = ""
        for key, value in student.items():
            info += f"{key}: {value}\n"
        self.results_text.insert(tk.END, info)

def main():
    root = tk.Tk()
    app = StudentSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
