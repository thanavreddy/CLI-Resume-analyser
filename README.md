#  CLI Resume Analyzer 

A simple and powerful command-line tool to analyze a resume PDF for key technical skills — perfect for data science, analytics, or engineering roles.

Built with Python and PyMuPDF (`fitz`), this tool helps job seekers tailor their resumes to match role-specific keywords.

---

##  Features

-  Extracts clean text from `.pdf` resumes
-  Counts how often important skills (like Python, SQL, ML) appear
-  Suggests missing skills based on popular industry keywords
-  Clean CLI interface using `argparse`
-  Outputs a skill table + keyword suggestions in terminal

---

## Requirements

- Python 3.7+
- pip (Python package manager)

### Install Dependencies

Inside a fresh virtual environment (recommended):

```bash
pip install PyMuPDF rich
```

---

##  Default Skill Keywords

The tool looks for these common skills:

```
Python, SQL, Machine Learning, Deep Learning, Data Analysis, 
Pandas, Numpy, Scikit-learn, TensorFlow, Keras
```

*(You can customize this list in analyzer.py)*

---

## ▶ How to Run

```bash
python main.py path/to/your_resume.pdf
```

**Example:**

```bash
python main.py resume124.pdf
```

You'll see a table of skill mentions and suggestions to improve.

---

## 🖼 Sample Output

![image](https://github.com/user-attachments/assets/1c516ce8-c701-4da0-8938-cb986edfab4d)


---

## 📁 Project Structure

```
resume-analyzer/
├── analyzer.py       # Logic for text extraction & skill analysis
├── main.py           # CLI entrypoint
├── sample_resume.pdf # (Optional) Sample resume to test
├── screenshot.png    # Example output
└── README.md
```

---

## 🎯 Usage Tips

- Place your resume PDF in the same directory as the script for easy access
- Use a virtual environment to avoid dependency conflicts
- Customize the skill keywords in `analyzer.py` to match your target roles
- Run the tool regularly when updating your resume to ensure key skills are highlighted



