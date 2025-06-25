import fitz  # PyMuPDF
from collections import Counter
from rich import print
from rich.table import Table

KEY_SKILLS = ["Python", "SQL", "Machine Learning", "Deep Learning", "Data Analysis",
              "Pandas", "Numpy", "Scikit-learn", "TensorFlow", "Keras","web development",]

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def count_skills(text):
    text_lower = text.lower()
    return {skill: text_lower.count(skill.lower()) for skill in KEY_SKILLS}

def suggest_improvements(skill_counts):
    missing = [skill for skill, count in skill_counts.items() if count == 0]
    if not missing:
        return "✅ Your resume covers all key skills!"
    return f"🔍 Consider adding: {', '.join(missing)}"

def analyze_resume(pdf_path):
    print(f"[bold green]📄 Analyzing:[/bold green] {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    skill_counts = count_skills(text)

    table = Table(title="Skill Match Report")
    table.add_column("Skill")
    table.add_column("Mentions", justify="center")

    for skill, count in skill_counts.items():
        table.add_row(skill, str(count))

    print(table)

    improvement_suggestion = suggest_improvements(skill_counts)
    print(f"\n[bold yellow]{improvement_suggestion}[/bold yellow]")
