@echo off

set SEVENZIP=C:\Program Files\7-Zip

rd /q /s appdir
pyinstaller app.spec
rd /q /s build
rd /q /s dist
rename app appdir

del BridgeShapeTool.zip
"%SEVENZIP%\7z.exe" a BridgeShapeTool.zip appdir\*