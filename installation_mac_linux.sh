#!/bin/bash

echo "========================================"
echo "  Ökobilanz-App - Installation"
echo "  Fachschule für Umweltschutztechnik"
echo "========================================"
echo ""
echo "Dieses Skript installiert alle benötigten Pakete."
echo "Bitte warten..."
echo ""

# Prüfen ob Python installiert ist
if ! command -v python3 &> /dev/null; then
    echo "[FEHLER] Python3 ist nicht installiert!"
    echo ""
    echo "Installation:"
    echo "  Mac:   brew install python3"
    echo "  Linux: sudo apt install python3 python3-pip"
    echo ""
    exit 1
fi

echo "[OK] Python gefunden: $(python3 --version)"
echo ""

echo "Installiere marimo..."
pip3 install marimo --quiet
echo "[OK] marimo installiert"

echo "Installiere pandas..."
pip3 install pandas --quiet
echo "[OK] pandas installiert"

echo "Installiere plotly..."
pip3 install plotly --quiet
echo "[OK] plotly installiert"

echo "Installiere altair..."
pip3 install altair --quiet
echo "[OK] altair installiert"

echo ""
echo "========================================"
echo "  Installation abgeschlossen!"
echo "========================================"
echo ""
echo "Nächste Schritte:"
echo "1. VS Code öffnen"
echo "2. marimo Extension installieren (falls nicht schon geschehen)"
echo "3. oekobilanz_app.py öffnen"
echo "4. Auf das marimo-Logo klicken"
echo ""
echo "Viel Erfolg!"
