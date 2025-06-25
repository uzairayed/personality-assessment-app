
import pandas as pd
import plotly.express as px
import preswald

# Load dataset
df = pd.read_csv("personality_synthetic_dataset.csv")

# Display header
from preswald import text, table, slider, plotly

text("# My Data Analysis App")

# Filter with SQL-style query (optional)
from preswald import query
sql = "SELECT * FROM personality_synthetic_dataset.csv WHERE curiosity > 5"
filtered_df = query(sql, "personality_synthetic_dataset.csv")
table(filtered_df, title="Filtered Data")

# Dynamic slider view
threshold = slider("Curiosity Threshold", min_val=0, max_val=10, default=5)
table(df[df["curiosity"] > threshold], title="Dynamic Data View: High Curiosity")

# 1. Bar Plot: Personality Type Counts
personality_counts = df["personality_type"].value_counts().rename_axis("personality_type").reset_index(name="count")
bar_plot = px.bar(
    personality_counts,
    x="personality_type",
    y="count",
    title="Distribution of Personality Types"
)

# 2. Box Plot: Trait Distributions by Personality Type
box_plot = px.box(
    df,
    x="personality_type",
    y="curiosity",
    color="personality_type",
    title="Distribution of Curiosity Across Personality Types"
)

# 3. Scatter Plot: Curiosity vs Creativity
scatter_plot = px.scatter(
    df,
    x="curiosity",
    y="creativity",
    color="personality_type",
    title="Curiosity vs Creativity by Personality Type",
    labels={"curiosity": "Curiosity", "creativity": "Creativity"}
)

# 4. Heatmap: Correlation Matrix of Traits
correlation_matrix = df.drop(columns=["personality_type"]).corr()
heatmap_plot = px.imshow(
    correlation_matrix,
    text_auto=True,
    color_continuous_scale="Viridis",
    title="Correlation Heatmap of Personality Traits"
)

# 5. Treemap: Proportion of Personality Types
treemap_data = personality_counts
treemap_plot = px.treemap(
    treemap_data,
    path=["personality_type"],
    values="count",
    title="Personality Type Proportion Treemap"
)

# 6. Report with Preswald
text("# Personality Trait Analysis")

text("## Personality Type Distribution")
plotly(bar_plot)

text("## Curiosity Trait Distribution by Type")
plotly(box_plot)

text("## Curiosity vs. Creativity Correlation")
plotly(scatter_plot)

text("## Correlation Matrix of Traits")
plotly(heatmap_plot)

text("## Treemap of Personality Types")
plotly(treemap_plot)
