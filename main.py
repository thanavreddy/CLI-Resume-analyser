import argparse
from analyzer import analyze_resume

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a resume PDF for key skill mentions.")
    parser.add_argument("pdf_path", type=str, help="Path to the resume PDF")
    args = parser.parse_args()

    analyze_resume(args.pdf_path)
