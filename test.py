import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium", html_head_file="head.html", app_title="marimo head bug")


@app.cell
def _():
    import marimo as mo

    mo.md("# Welcome to marimo! 🌊🍃")
    return (mo,)

