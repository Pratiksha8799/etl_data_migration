@echo off
cd /d "<path_to_file>"
python upload_bigquery.py >> "<path_to_file>\migration.log" 2>&1
pause
