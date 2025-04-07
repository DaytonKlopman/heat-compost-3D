import pandas as pd
import plotly.express as px

df = pd.read_csv('Phosphorus Heat Compost - Sheet1.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
df['Formatted_Date'] = df['Date'].dt.strftime('%m/%d/%y')

fig = px.scatter_3d(df, x='Phosphorus(%)', y='Moisture(%)', z='pH(1:2)', color='Formatted_Date',
                    title="3D Scatter Plot of Phosphorus, Moisture, and pH",
                    color_continuous_scale='Viridis')

fig.update_layout(
    scene=dict(
        xaxis_title='Phosphorus (%)',
        yaxis_title='Moisture (%)',
        zaxis_title='pH(1:2)',
        xaxis=dict(range=[df['Phosphorus(%)'].min() - 0.1, df['Phosphorus(%)'].max() + 0.1]),
        yaxis=dict(range=[df['Moisture(%)'].min() - 0.1, df['Moisture(%)'].max() + 0.1]),
        zaxis=dict(range=[df['pH(1:2)'].min() - 0.1, df['pH(1:2)'].max() + 0.1]),
    ),
    coloraxis_colorbar=dict(
        title='Date',
        tickvals=df['Formatted_Date'].unique(),
    )
)

fig.show()