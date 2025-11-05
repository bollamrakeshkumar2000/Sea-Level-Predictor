
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label='Data')
    
    # Get first and last year for calculations
    first_year = df['Year'].min()
    last_year = df['Year'].max()
    
    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend years to 2050 for prediction
    years_extended = np.arange(first_year, 2051)
    
    # Calculate sea level rise for first line
    sea_levels_extended = slope * years_extended + intercept
    
    # Plot first line of best fit
    plt.plot(years_extended, sea_levels_extended, 'r', label='Best Fit Line (1880-2013)')
    
    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Extend recent years to 2050 for prediction
    years_recent_extended = np.arange(2000, 2051)
    
    # Calculate sea level rise for second line
    sea_levels_recent_extended = slope_recent * years_recent_extended + intercept_recent
    
    # Plot second line of best fit
    plt.plot(years_recent_extended, sea_levels_recent_extended, 'g', label='Best Fit Line (2000-2013)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gcf()

# Run the function if script is executed directly
if __name__ == "__main__":
    draw_plot()
    plt.show()
