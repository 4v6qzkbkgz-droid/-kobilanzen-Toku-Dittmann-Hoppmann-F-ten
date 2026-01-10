@echo off
echo ========================================
echo   Oekobilanz-App - Installation
echo   Fachschule fuer Umweltschutztechnik
echo ========================================
echo.
echo Dieses Skript installiert alle benoetigten Pakete.
echo Bitte warten...
echo.

REM Prüfen ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo [FEHLER] Python ist nicht installiert oder nicht im PATH!
    echo.
    echo Bitte installiere Python von https://python.org
    echo WICHTIG: Bei der Installation "Add Python to PATH" ankreuzen!
    echo.
    pause
    exit /b 1
)

echo [OK] Python gefunden
echo.

echo Installiere marimo...
pip install marimo --quiet
if errorlevel 1 (
    echo [FEHLER] marimo konnte nicht installiert werden
    pause
    exit /b 1
)
echo [OK] marimo installiert

echo Installiere pandas...
pip install pandas --quiet
echo [OK] pandas installiert

echo Installiere plotly...
pip install plotly --quiet
echo [OK] plotly installiert

echo Installiere altair...
pip install altair --quiet
echo [OK] altair installiert

echo.
echo ========================================
echo   Installation abgeschlossen!
echo ========================================
echo.
echo Naechste Schritte:
echo 1. VS Code oeffnen
echo 2. marimo Extension installieren (falls nicht schon geschehen)
echo 3. oekobilanz_app.py oeffnen
echo 4. Auf das marimo-Logo klicken
echo.
echo Viel Erfolg!
echo.
pause
