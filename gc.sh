git ls-files >../paths-i-want.txt
python3 .\git-filter-repo.txt --force --paths-from-file ..\paths-i-want.txt