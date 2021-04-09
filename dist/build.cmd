@echo off

set SEVENZIP=D:\7ZIP\7-Zip

rd /q /s appdir
pyinstaller app.spec
rd /q /s build
rd /q /s dist
rename app appdir

del BridgeShapeTool.exe
"%SEVENZIP%\7z.exe" -sfx7zS2.sfx -m0=Copy a BridgeShapeTool.exe appdir\*