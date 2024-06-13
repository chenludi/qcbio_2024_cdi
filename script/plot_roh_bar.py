import os
import matplotlib
matplotlib.use('Agg')  # Use Agg backend, which does not require a display
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

def plot_roh(input_file):
    # Read the input file into a DataFrame
    df = pd.read_csv(input_file, delim_whitespace=True)

    # Plot the bar plot for the KB column
    plt.figure(figsize=(10, 6))
    plt.bar(df['IID'], df['KB'], color='skyblue')
    plt.xlabel('Individual ID')
    plt.ylabel('Length of ROH (KB)')
    plt.title('Length of ROH in Kilobases for Each Individual')
    plt.xticks(rotation=45, ha='right')
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


