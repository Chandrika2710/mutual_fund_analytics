from pathlib import Path
import subprocess
import sys

project_root = Path(__file__).resolve().parent.parent
scripts = project_root / "scripts"

pipeline = [
    "data_ingestion.py",
    "clean_nav.py",
    "clean_performance.py",
    "clean_transaction.py",
    "download_benchmark.py",
    "load_to_sqlite.py"
]

print("=" * 50)
print("Starting ETL Pipeline")
print("=" * 50)

for script in pipeline:
    script_path = scripts / script

    if script_path.exists():
        print(f"\nRunning {script} ...")

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{script} completed successfully.")
        else:
            print(f"{script} failed.")
            print(result.stderr)

    else:
        print(f"{script} not found.")

print("\nETL Pipeline Completed Successfully.")