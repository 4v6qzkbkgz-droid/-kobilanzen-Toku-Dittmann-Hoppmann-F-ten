#!/bin/bash

# ===========================================
# marimo Starter - Doppelklick zum Starten
# ===========================================

# In den Ordner wechseln, wo dieses Skript liegt
cd "$(dirname "$0")"

echo "🌱 Starte marimo..."
echo ""
echo "Die App öffnet sich gleich im Browser."
echo "Dieses Fenster kann offen bleiben."
echo ""
echo "Zum Beenden: Strg+C drücken oder Fenster schließen."
echo ""

# marimo starten
python3 -m marimo edit starter_app.py
