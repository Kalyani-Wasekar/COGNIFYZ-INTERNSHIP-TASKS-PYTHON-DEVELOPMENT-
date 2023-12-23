import pandas as pd
import plotly.express as px

def generate_interactive_plot(dataset_path):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Check if the dataset has numerical columns
    numerical_columns = df.select_dtypes(include=['number']).columns
    if not numerical_columns:
        print("No numerical columns found in the dataset.")
        return

    # Get user input for the columns to plot
    print("Choose columns for X and Y axes from the following:")
    for i, col in enumerate(numerical_columns):
        print(f"{i + 1}. {col}")

    x_col_index = int(input("Enter the index of the X-axis column: ")) - 1
    y_col_index = int(input("Enter the index of the Y-axis column: ")) - 1

    x_col = numerical_columns[x_col_index]
    y_col = numerical_columns[y_col_index]

    # Create an interactive scatter plot using Plotly Express
    fig = px.scatter(df, x=x_col, y=y_col, title=f"Interactive Scatter Plot: {x_col} vs {y_col}",
                     labels={x_col: x_col, y_col: y_col}, hover_name=df.index)

    # Show the plot
    fig.show()

if __name__ == "__main__":
    dataset_path = input("Enter the path to your dataset (CSV format): ")
    generate_interactive_plot(dataset_path)
