cd client

echo creating executable...

pyinstaller -c -F main.spec
cd ..

echo pushing to git...

git add .
git commit -m "hot-fix"
git push -u origin main

echo finished