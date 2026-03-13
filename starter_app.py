import marimo

__generated_with = "0.19.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    # Weitere Imports hier ergänzen (z.B. plotly)
    return alt, mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # 🌱 Ökobilanz-App für Erneuerbare Energien

    **Entwickelt von: [EUER GRUPPENNAME]**

    Kurze Beschreibung eurer App hier einfügen...

    ---
    """)
    return


@app.cell
def _():
    # =================================================================
    # DATEN
    # =================================================================
    # Hier eure Daten einfügen
    # 
    # Tipp: Recherchiert auf https://www.probas.umweltbundesamt.de
    # 
    # Beispielstruktur:
    # energietraeger_daten = pd.DataFrame({
    #     "Energieträger": ["Photovoltaik", "Windkraft", ...],
    #     "CO2_eq_g_kWh": [40, 10, ...],
    #     ...
    # })

    # TODO: Eure Daten hier einfügen
    #energietraeger_daten = pd.DataFrame({
    #    "Energieträger": ["Beispiel 1", "Beispiel 2"],
    #    "CO2_eq_g_kWh": [0, 0],
        # Weitere Spalten ergänzen...
    #})
    return


@app.cell
def _(pd):
    # Beispieldaten angelehnt an ProBas/GEMIS-Werte
    # Quelle: Typische Werte aus Lebenszyklusanalysen

    energietraeger_daten = pd.DataFrame({
        "Energieträger": [
            "Photovoltaik (Dach)", 
            "Photovoltaik (Freifläche)",
            "Windkraft (Onshore)", 
            "Windkraft (Offshore)",
            "Wasserkraft (Laufwasser)",
            "Biomasse (Holz-HKW)",
            "Biogas (landw.)",
            "Solarthermie",
            "Geothermie"
        ],
        "CO2_eq_g_kWh": [40, 35, 10, 12, 4, 30, 170, 25, 38],  # g CO2-eq/kWh
        "KEA_MJ_kWh": [0.45, 0.40, 0.08, 0.10, 0.02, 0.15, 0.85, 0.30, 0.42],  # MJ/kWh kumulierter Energieaufwand
        "Flaechenbedarf_m2_kW": [7, 20, 30, 15, 0.5, 500, 300, 3, 2],  # m²/kW installierte Leistung
        "Lebensdauer_Jahre": [25, 25, 20, 25, 80, 20, 15, 20, 30],
        "Erntefaktor": [10, 12, 50, 45, 200, 8, 3, 15, 12],  # Energy Return on Investment
        "Kategorie": [
            "Solar", "Solar", "Wind", "Wind", "Wasser", 
            "Biomasse", "Biomasse", "Solar", "Geothermie"
        ]
    })
    energietraeger_daten
    return (energietraeger_daten,)


@app.cell
def _(alt, energietraeger_daten):
    # Diagramm erstellen, Code mit dataframe gui erstellt
    _chart = (
        alt.Chart(energietraeger_daten)
        .mark_point()
        .encode(
            x=alt.X(field='Energieträger', type='nominal'),
            y=alt.Y(field='CO2_eq_g_kWh', type='quantitative', aggregate='mean'),
            tooltip=[
                alt.Tooltip(field='Energieträger'),
                alt.Tooltip(field='CO2_eq_g_kWh', aggregate='mean', format=',.0f')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': True
                }
            }
        )
    )
    _chart
    return


@app.cell
def _(energietraeger_daten, mo):
    # =================================================================
    # BENUTZEROBERFLÄCHE (UI)
    # =================================================================
    # Hier interaktive Elemente erstellen
    #
    # Beispiele:
    # - Dropdown: mo.ui.dropdown(options=[...], label="...")
    # - Slider:   mo.ui.slider(start=0, stop=100, value=50, label="...")
    # - Checkbox: mo.ui.checkbox(label="...")
    #
    # Dokumentation: https://docs.marimo.io/api/inputs/

    # TODO: Eure UI-Elemente hier erstellen

    # Beispiel Dropdown:
    energie_auswahl = mo.ui.dropdown(
        options=energietraeger_daten["Energieträger"].tolist(),
        value=energietraeger_daten["Energieträger"].iloc[0],
        label="Energieträger auswählen"
    )

    # Beispiel Slider:
    leistung_slider = mo.ui.slider(start=1, stop=1000, value=100, label="Leistung (kW)")
    return energie_auswahl, leistung_slider


@app.cell
def _(energie_auswahl, leistung_slider, mo):
    mo.md(f"""
    ## ⚙️ Parameter einstellen

    {mo.hstack([energie_auswahl, leistung_slider], justify="start", gap=2)}
    """)
    return


@app.cell
def _(energie_auswahl, energietraeger_daten, leistung_slider):
    # =================================================================
    # BERECHNUNGEN
    # =================================================================
    # Hier die Berechnungen basierend auf der Auswahl durchführen
    #
    # Beispiel:
    # ausgewaehlter_traeger = energie_auswahl.value
    # daten = energietraeger_daten[energietraeger_daten["Energieträger"] == ausgewaehlter_traeger]
    # co2_wert = daten["CO2_eq_g_kWh"].iloc[0]

    # TODO: Eure Berechnungen hier

    ausgewaehlter_traeger = energie_auswahl.value
    leistung_kw=leistung_slider.value
    jahresertrag_kwh = leistung_kw * 1100 #1000 nur als Beispiel

    # Beispiel: Daten für ausgewählten Träger holen
    daten = energietraeger_daten[
        energietraeger_daten["Energieträger"] == ausgewaehlter_traeger
    ].iloc[0]
    return ausgewaehlter_traeger, jahresertrag_kwh, leistung_kw


@app.cell
def _(ausgewaehlter_traeger, jahresertrag_kwh, leistung_kw, mo):
    mo.md(f"""
    ## 📊 Ergebnisse für {ausgewaehlter_traeger}

    ### Energieertrag
    | Kennzahl | Wert |
    |----------|------|
    | Installierte Leistung | **{leistung_kw:,.0f} kW** |
    | Jahresertrag | **{jahresertrag_kwh:,.0f} kWh/a** |
    """)
    return


@app.cell
def _(mo):
    # =================================================================
    # VISUALISIERUNG
    # =================================================================
    # Hier Diagramme erstellen
    #
    # Möglichkeiten:
    # - plotly: Interaktive Diagramme (empfohlen)
    #   import plotly.express as px
    #   fig = px.bar(df, x="...", y="...")
    #   mo.ui.plotly(fig)
    #
    # - matplotlib: Statische Diagramme
    #   import matplotlib.pyplot as plt
    #   plt.bar(...)
    #   plt.gcf()
    #
    # Dokumentation: https://docs.marimo.io/api/plotting/

    # TODO: Eure Visualisierungen hier

    mo.md("""
    ## 📈 Visualisierung

    *Hier kommen eure Diagramme hin...*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ## ℹ️ Hinweise

    **Datenquellen:**
    - [Hier eure Quellen angeben]

    **Methodik:**
    - [Hier eure Methodik beschreiben]

    ---

    *Entwickelt für die Fachschule für Umweltschutztechnik*
    """)
    return


if __name__ == "__main__":
    app.run()
