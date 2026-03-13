import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    return mo, plt


@app.cell
def _(mo):
    cb_pv = mo.ui.checkbox(label="Photovoltaik anzeigen", value=True)
    cb_wind = mo.ui.checkbox(label="Windkraft anzeigen", value=True)
    cb_water = mo.ui.checkbox(label="Wasserkraft anzeigen", value=False)
    cb_bio = mo.ui.checkbox(label="Biogas anzeigen", value=False)

    pv_slider = mo.ui.slider(start=0, stop=2000, value=800, step=50, label="PV Strom (GWh/Jahr)")
    wind_slider = mo.ui.slider(start=0, stop=2000, value=600, step=50, label="Wind Strom (GWh/Jahr)")
    water_slider = mo.ui.slider(start=0, stop=2000, value=300, step=50, label="Wasser Strom (GWh/Jahr)")
    bio_slider = mo.ui.slider(start=0, stop=2000, value=200, step=50, label="Biogas Strom (GWh/Jahr)")

    metric = mo.ui.radio(
        options=[
            "Emissionsintensität (gCO₂e/kWh)",
            "Gesamtemissionen (tCO₂e/Jahr)"
        ],
        value="Gesamtemissionen (tCO₂e/Jahr)",
        label="Anzeige"
    )

    fossil_choice = mo.ui.radio(
        options=["Gas", "Kohle"],
        value="Gas",
        label="Fossiler Vergleich"
    )

    mo.vstack([
        mo.md("# 🌍 Interaktive Energiesystem-Simulation"),
        cb_pv, cb_wind, cb_water, cb_bio,
        pv_slider, wind_slider, water_slider, bio_slider,
        fossil_choice,
        metric
    ])

    return (
        bio_slider,
        cb_bio,
        cb_pv,
        cb_water,
        cb_wind,
        fossil_choice,
        metric,
        pv_slider,
        water_slider,
        wind_slider,
    )


@app.cell
def _(
    bio_slider,
    cb_bio,
    cb_pv,
    cb_water,
    cb_wind,
    fossil_choice,
    metric,
    mo,
    plt,
    pv_slider,
    water_slider,
    wind_slider,
):
    intensity = {
        "PV": 48,
        "Wind": 11,
        "Wasser": 24,
        "Biogas": 230
    }

    fossil_intensity = {
        "Gas": 490,
        "Kohle": 820
    }

    def total_tco2e(g_per_kwh, gwh):
        return g_per_kwh * gwh

    labels = []
    values = []
    total_emissions = 0
    total_production = 0

    is_intensity = "Intensität" in metric.value

    if cb_pv.value:
        emission = total_tco2e(intensity["PV"], pv_slider.value)
        labels.append("PV")
        values.append(intensity["PV"] if is_intensity else emission)
        total_emissions += emission
        total_production += pv_slider.value

    if cb_wind.value:
        emission = total_tco2e(intensity["Wind"], wind_slider.value)
        labels.append("Wind")
        values.append(intensity["Wind"] if is_intensity else emission)
        total_emissions += emission
        total_production += wind_slider.value

    if cb_water.value:
        emission = total_tco2e(intensity["Wasser"], water_slider.value)
        labels.append("Wasser")
        values.append(intensity["Wasser"] if is_intensity else emission)
        total_emissions += emission
        total_production += water_slider.value

    if cb_bio.value:
        emission = total_tco2e(intensity["Biogas"], bio_slider.value)
        labels.append("Biogas")
        values.append(intensity["Biogas"] if is_intensity else emission)
        total_emissions += emission
        total_production += bio_slider.value

    fossil_g = fossil_intensity[fossil_choice.value]
    fossil_emissions = total_tco2e(fossil_g, total_production)
    co2_savings = fossil_emissions - total_emissions

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("gCO₂e/kWh" if is_intensity else "tCO₂e/Jahr")
    ax.set_title("Emissionen der aktivierten Energieträger")
    ax.grid(True, axis="y", linestyle="--", linewidth=0.5)
    plt.tight_layout()

    mo.vstack([
        mo.pyplot(fig),
        mo.callout(
            f"Gesamtproduktion: {total_production:.0f} GWh/Jahr\n"
            f"Emissionen erneuerbar: {total_emissions:.0f} tCO₂e/Jahr\n"
            f"Emissionen {fossil_choice.value}: {fossil_emissions:.0f} tCO₂e/Jahr\n"
            f"➡️ CO₂-Einsparung: {co2_savings:.0f} tCO₂e/Jahr",
            kind="success" if co2_savings > 0 else "warning"
        )
    ])

    return


if __name__ == "__main__":
    app.run()
