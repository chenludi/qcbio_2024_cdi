import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

def plot_roh(input_file):
    # Read the input file into a DataFrame
    df = pd.read_csv(input_file, delim_whitespace=True)

    # Plot the horizontal bar plot for the ROH regions
    plt.figure(figsize=(10, 6))
    for index, row in df.iterrows():
        plt.barh(row['IID'], row['POS2'] - row['POS1'], left=row['POS1'], color='skyblue')

    plt.xlabel('Genome Coordinate')
    plt.ylabel('Individual ID')
    plt.title('ROH Regions for Each Individual')
    plt.tight_layout()

    # Create the output file name based on the input file name
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_roh_plot.pdf"
    
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

    input_file = sys.argv[1]
    plot_roh(input_file)

