import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Generating random data for 1000 students and their departments
np.random.seed(0)
num_students = 1000
departments = ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science']
student_department = np.random.choice(departments, num_students)
student_grades = np.random.randint(50, 101, num_students)

# Counting number of students in each department
department_counts = {dept: np.sum(student_department == dept) for dept in departments}

# Normalize data for pie chart
total_students = sum(department_counts.values())
percentages = [count / total_students * 100 for count in department_counts.values()]
labels = [f"{dept} ({percentage:.1f}%)" for dept, percentage in zip(departments, percentages)]

def show_summary():
    summary = """
    Hello! I'm Hariom, a cheerful 🎓 Computer Science Engineering student at Excel Engineering College. 
    I love tech and coding, and I'm always up for fun challenges that help me learn and grow.
    
    🚀 What I Do:
    
    I spend my days working on cool projects and practicing coding. 
    You'll often find me on sites like HackerRank, LeetCode, GeekforGeeks, and Coding Ninjas, sharpening my skills.
    
    💼 Skills & Expertise:
    
    I'm good at making websites 💻, coding in Java ☕, and using Python 🐍. 
    I've finished lots of projects that show off what I can do.
    
    🌟 My Confidence Booster:
    
    I'm really good at solving tough problems! 
    On LeetCode, I have a 3.5⭐️ rating, on HackerRank, I've got 5⭐️, and on GeekforGeeks & CodingNinjas, I've scored over 700. 
    It's fun for me to figure things out and find solutions.
    
    💡 Always Learning:
    
    I'm always curious and excited to learn new things and try out the latest technologies. 
    Each new thing I discover feels like an adventure!
    
    🔍 Future Goals:
    
    My dream is to become a software architect. 
    With determination and a love for learning, I'm ready to take on any challenge that comes my way.
    """
    messagebox.showinfo("Student Summary", summary)

# Plotting both bar graph and pie chart on the same page
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotting bar graph
ax1.bar(department_counts.keys(), department_counts.values(), color='skyblue')
ax1.set_title('Number of Students in Each Department')
ax1.set_xlabel('Departments')
ax1.set_ylabel('Number of Students')
ax1.tick_params(axis='x', rotation=45)

# Plotting pie chart
ax2.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140)
ax2.set_title('Percentage of Students in Each Department')

# Create a Tkinter window
root = Tk()
root.title("Student Management System")

# Embedding matplotlib plots in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Adding toolbar for navigation
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack()

# Create a button to display summary
summary_button = Button(root, text="Show My Summary", command=show_summary)
summary_button.pack()

# Run Tkinter event loop
root.mainloop()
