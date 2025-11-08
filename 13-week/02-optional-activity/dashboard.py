
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load dataset
df = pd.read_excel("dataset_ventas.xlsx")

app = Dash(__name__)

# Total sales KPI
total_sales = df["TotalVenta"].sum()

app.layout = html.Div(children=[
    html.H1("Tablero de Ventas", style={'textAlign':'center'}),
    html.H2(f"Ventas Totales: ${total_sales:,.2f}", style={'color':'blue'}),

    dcc.Graph(
        figure=px.bar(df.groupby("Producto")["TotalVenta"].sum().reset_index(),
            x="Producto", y="TotalVenta", title="Ventas por Producto")
    ),

    dcc.Graph(
        figure=px.line(df.groupby("Fecha")["TotalVenta"].sum().reset_index(),
            x="Fecha", y="TotalVenta", title="Evolución de Ventas en el Tiempo")
    ),

    dcc.Graph(
        figure=px.bar(df.groupby("Cliente")["TotalVenta"].sum().reset_index(),
            x="Cliente", y="TotalVenta", title="Clientes más Rentables")
    ),

    dcc.Graph(
        figure=px.scatter(df, x="Cantidad", y="TotalVenta", color="Región",
            title="Relación Cantidad vs Total de Venta por Región")
    )
])

if __name__ == "__main__":
    app.run(debug=True)
