import os
import pdfplumber
import re
import nltk
from tkinter import Tk, Label, Button, filedialog, messagebox, Toplevel, Text

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Default required skills
required_skills = ['Python', 'SQL', 'Data Analysis', 'Machine Learning', 'Excel']

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text

# Function to clean text by removing stopwords and special characters
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\d', ' ', text)  # Remove numbers
    words = text.lower().split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

# Function to check if required skills are present in the resume
def check_skills_in_resume(resume_text, required_skills):
    present_skills = []
    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            present_skills.append(skill)
    return present_skills

# Function to upload resume and check for skills
def upload_and_check():
    file_path = filedialog.askopenfilename(title="Select Resume", filetypes=[("PDF files", "*.pdf")])
    
    if file_path:
        resume_text = extract_text_from_pdf(file_path)
        cleaned_resume_text = clean_text(resume_text)
        matched_skills = check_skills_in_resume(cleaned_resume_text, required_skills)
        
        if matched_skills:
            messagebox.showinfo("Matched Skills", f"Skills found: {', '.join(matched_skills)}")
        else:
            messagebox.showinfo("No Skills Found", "No required skills were found in the resume.")

# Function to open a new window to edit the required skills
def edit_skills():
    # Create a new window for editing skills
    skills_window = Toplevel(root)
    skills_window.title("Edit Required Skills")
    skills_window.geometry("400x300")
    
    Label(skills_window, text="Enter Required Skills (comma-separated):").pack(pady=10)
    
    # Text box for entering skills
    skills_textbox = Text(skills_window, height=10, width=50)
    skills_textbox.pack(pady=10)
    
    # Pre-fill the text box with the current skills
    skills_textbox.insert("1.0", ', '.join(required_skills))
    
    # Function to save edited skills
    def save_skills():
        global required_skills
        # Get the skills from the text box, split by commas, and strip whitespaces
        new_skills = skills_textbox.get("1.0", "end-1c").split(',')
        required_skills = [skill.strip() for skill in new_skills if skill.strip()]
        messagebox.showinfo("Skills Updated", "Required skills have been updated.")
        skills_window.destroy()
    
    # Save button to save new skills
    Button(skills_window, text="Save Skills", command=save_skills).pack(pady=10)

# Create Tkinter window
root = Tk()
root.title("Resume Skill Checker")
root.geometry("300x200")

# Create button for uploading resume
Label(root, text="Upload Resume and Check Skills").pack(pady=20)
Button(root, text="Upload Resume", command=upload_and_check).pack(pady=10)

# Button to edit required skills
Button(root, text="Set Required Skills", command=edit_skills).pack(pady=10)

# Run the Tkinter loop
root.mainloop()
