@echo off
setlocal EnableExtensions EnableDelayedExpansion

if not exist ".venv" (
    python --version > nul 2>&1
    if %errorlevel% equ 0 (
        set /P "answer=Nao tens virtual environment, queres criar um novo? (y/n):"

        if /i "!answer!" == "y" (
            echo A criar...
            python -m venv .venv
            call .venv\Scripts\activate.bat
            python.exe -m pip install --upgrade pip
            pip install Flask
        ) else (
            exit
        )
    ) else (
        echo "Nao tens python instalado"
        exit
    )
)

set "answer=n"
set /p answer= "Ja tens o virtual environment criado, queres abrir o site? (y/n):"
if /i "!answer!"=="y" (
    call .venv\Scripts\activate.bat
    flask run
    exit
)