import os
import glob
import subprocess
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# ------------------------------
# CLEAN ALL CSV FILES
# ------------------------------
def clean_csv_folders(folders):
    print("🧹 Cleaning all CSV files in data folders...")
    for folder in folders:
        for file in glob.glob(os.path.join(folder, "*.csv")):
            os.remove(file)
    print("✅ All previous CSVs deleted.\n")

# ------------------------------
# RUN PYTHON SCRIPT SEQUENTIALLY
# ------------------------------
def run_script(script_path):
    print(f"▶️ Running: {script_path}")
    try:
        subprocess.run(["python3", script_path], check=True)
        print(f"✅ Completed: {script_path}\n")
    except subprocess.CalledProcessError:
        print(f"❌ Failed at step: {script_path}")
        exit(1)

# ------------------------------
# RUN JUPYTER NOTEBOOK
# ------------------------------
def run_notebook(notebook_path):
    print(f"📓 Executing notebook: {notebook_path}")
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    print("✅ Notebook executed.\n")

# ------------------------------
# MAIN PIPELINE RUN
# ------------------------------
if __name__ == "__main__":
    clean_csv_folders(["../data/raw", "../data/processed", "../data/merged", "../data/reports"])

    # 1. Generate Raw Data
    for script in sorted(glob.glob("../generate_data/*.py")):
        run_script(script)


    # 2. Preprocess Feature Scripts
    for script in sorted(glob.glob("../preprocess/feature_*.py")):
        run_script(script)
        run_script("../preprocess/time_series_engineer.py")


    # 3. Merge Features
    run_script("../preprocess/merge_all_features.py")

    # 4. Models - Cluster & Risk
    for script in sorted(glob.glob("../models/*.py")):
        run_script(script)

    # 5. Run Notebooks (optional EDA)
    run_notebook("../notebooks/eda_final.ipynb")

    # 6. Reports
    for script in sorted(glob.glob("../reports/*.py")):
        run_script(script)

    # 7. Scoring (CQI computation & export)
    for script in sorted(glob.glob("../scoring/*.py")):
        run_script(script)

    print("🎉 Full pipeline completed successfully!")
