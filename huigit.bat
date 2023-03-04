@echo off
if [%1]==[] goto usage

git add .
git commit -m %1
git pull
git push
goto :eof
:usage
@echo Please add a comment

