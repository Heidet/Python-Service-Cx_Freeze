@echo OFF
powershell write-host -fore Green =======================================================================================
powershell write-host -fore Green NAME: compile_convd_windows.bat
powershell write-host -fore Green AUTHOR: Heidet Antoine
powershell write-host -fore Green DATE: 24/08/2021
powershell write-host -fore Green COMPILE: Compilation MSI + EXE + freeze packages
powershell write-host -fore Green VERSION 1.X
powershell write-host -fore Green Script automatisation compilation convd_service python39 avec PYC, modules et packages
powershell write-host -fore Green =======================================================================================
timeout /t 30


powershell write-host -fore Cyan Freeze modules pip
python39 -m pip freeze > requirements.txt
timeout /t 5

powershell write-host -fore Cyan Copie requirements.txt dans convd-release pour ajout dans les repertoires de compilation
copy requirements.txt convd-release
timeout /t 5

powershell write-host -fore Cyan Copie module convd_service dans win32 pour compilation
copy convd_service.py win32
timeout /t 5

powershell write-host -fore Cyan Repertoire win32 pour compilation windows
cd win32
timeout /t 5

powershell write-host -fore Cyan Compilation de l'executable exe
python39 setup.py build -b ../convd-release/win32
timeout /t 5

powershell write-host -fore Cyan Compilation PYC
python39 compile_pyc.py
timeout /t 5


powershell write-host -fore Red Suppression du module convd_service
del convd_service.py


powershell write-host -fore Red Suppression du repertoire dist et la Suppression du repertoire build
rmdir /s /q build

cd ..
