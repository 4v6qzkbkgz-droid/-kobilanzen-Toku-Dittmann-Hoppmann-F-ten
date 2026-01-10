# 🌱 Ökobilanz-App für Erneuerbare Energien

Eine interaktive App zur Berechnung und Visualisierung von Lebenszyklusanalysen (Ökobilanzen) verschiedener erneuerbarer Energieträger.

**Entwickelt von der Fachschule für Umweltschutztechnik**

---

## 🚀 Schnellstart

### 1. Repository klonen

In **GitHub Desktop**:
- File → Clone Repository → URL eingeben

### 2. Pakete installieren

**Windows:** Doppelklick auf `installation_windows.bat`

**Mac/Linux:** Terminal öffnen und ausführen:
```bash
chmod +x installation_mac_linux.sh
./installation_mac_linux.sh
```

### 3. App starten

1. **VS Code** öffnen
2. Datei `oekobilanz_app.py` öffnen
3. Auf das **marimo-Logo** 🌿 klicken (oben rechts)
4. **"Start in marimo editor"** wählen

---

## 📊 Features

- **Vergleich von 9 Energieträgern:** Photovoltaik, Wind, Wasser, Biomasse, Geothermie
- **Interaktive Parameter:** Leistung, Volllaststunden, Betrachtungszeitraum
- **Umweltkennzahlen:** CO₂-Äquivalente, Kumulierter Energieaufwand, Erntefaktor, Flächenbedarf
- **Visualisierungen:** Vergleichsdiagramme und Nachhaltigkeits-Radar-Chart
- **CO₂-Einsparung:** Vergleich zum deutschen Strommix

---

## 📁 Projektstruktur

```
oekobilanz-app/
├── oekobilanz_app.py          # Haupt-App (marimo notebook)
├── requirements.txt           # Python-Abhängigkeiten
├── installation_windows.bat   # Installer für Windows
├── installation_mac_linux.sh  # Installer für Mac/Linux
├── anleitung_ohne_kommandozeile.md  # Schüler-Anleitung
└── README.md                  # Diese Datei
```

---

## 🤝 Gemeinsam arbeiten

1. **Vor dem Arbeiten:** In GitHub Desktop → "Fetch origin" → "Pull origin"
2. **Bearbeiten:** In VS Code mit marimo Extension
3. **Testen:** marimo-Logo → "Start in run mode"
4. **Teilen:** In GitHub Desktop → Commit → Push

Siehe `anleitung_ohne_kommandozeile.md` für die vollständige Anleitung.

---

## 📚 Datenquellen

- [ProBas - Umweltbundesamt](https://www.probas.umweltbundesamt.de/) 
- GEMIS (Globales Emissions-Modell integrierter Systeme)

**Hinweis:** Die aktuellen Daten sind Beispielwerte. Für offizielle Ökobilanzen sollten aktuelle ProBas-Daten verwendet werden.

---

## 🛠️ Technologie

- **[marimo](https://marimo.io/)** - Reaktives Python-Notebook
- **[pandas](https://pandas.pydata.org/)** - Datenverarbeitung
- **[plotly](https://plotly.com/)** - Interaktive Visualisierungen

---

## 📄 Lizenz

Dieses Projekt ist für Bildungszwecke erstellt.

---

*Fachschule für Umweltschutztechnik*
