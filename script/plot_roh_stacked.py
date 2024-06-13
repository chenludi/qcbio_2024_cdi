import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os

def plot_roh(input_file):
    # Read the input file into a DataFrame
    df = pd.read_csv(input_file, delim_whitespace=True)

    # Sample data for the plot (assuming this comes from the input file)
    data = {
        'IID': df['IID'].tolist(),
        '0.1-1Mb': [300, 400, 500],  # Placeholder data; replace with actual
        '1-10Mb': [500, 300, 400],   # Placeholder data; replace with actual
        '>10Mb': [370, 385.035, 190.861]  # Placeholder data; replace with actual
    }

    df = pd.DataFrame(data)

    # Plot the stacked bar plot for the ROH regions
    fig, ax = plt.subplots(figsize=(10, 6))

    # Define the categories
    categories = ['>10Mb', '1-10Mb', '0.1-1Mb']
    colors = ['darkgreen', 'mediumseagreen', 'lightgreen']

    # Create stacked bars
    bottoms = np.zeros(len(df))
    for category, color in zip(categories, colors):
        ax.bar(df['IID'], df[category], bottom=bottoms, label=category, color=color)
        bottoms += df[category]

    # Add labels and title
    ax.set_xlabel('Individual ID')
    ax.set_ylabel('Summed ROH length (Mb)')
    ax.set_title('Summed ROH Length by Category')
    ax.legend(title='ROH Length')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Create the output file name based on the input file name
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_stacked_roh_plot.pdf"
    
    # Save the plot as a PDF
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Check if the script received the input file as an argument
    if len(sys.argv) != 2:
        print("Usage: python plot_roh.py <input_file>")
        sys.exit(1)


