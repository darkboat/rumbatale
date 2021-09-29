cd client

echo creating executable...

pyinstaller --onefile --windowed --icon=C:\Users\mikae\Documents\vscode\python\rumbatale\resources\static\icon.ico main.spec

cd ../installer

pyinstaller --onefile main.py

cd ../launcher

pyinstaller --onefile main.py

cd ..

echo pushing to git...

git add .
git commit -m "hot-fix"
git push -u origin main

cd installer
python main.py
cd ..

echo finished