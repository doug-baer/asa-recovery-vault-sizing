import numpy as np
import matplotlib.pyplot as plt

# Data points from VLR Planner: (time in minutes, change rate in %)
x_data = np.array([240.0, 1440.0, 10080.0, 43800.0])
y_data = np.array([0.5, 1.0, 2.5, 10.0])

REGULAR_PLOT = False

def fit_power_law(x, y):
    # Take the natural log of the data
    log_x = np.log(x)
    log_y = np.log(y)
    
    # Linear regression on log-transformed data
    slope, intercept = np.polyfit(log_x, log_y, 1)
    
    # Convert back to power law parameters
    b = slope
    a = np.exp(intercept)
    
    return a, b

a, b = fit_power_law(x_data, y_data)

print("--- Power Law Fit Results ---")
print(f"Scaling factor (a): {a:.4f}")
print(f"Exponent       (b): {b:.4f}")
print(f"Equation          : y = {a:.5f} * x^{b:.4f}\n")


# --- PLOTTING ON A LOG-LOG SCALE ---
# Using np.logspace ensures smooth line plotting on a logarithmic scale
x_curve = np.logspace(np.log10(min(x_data) * 0.8), np.log10(max(x_data) * 1.2), 500)
y_curve = a * (x_curve ** b)

# plot original data points
plt.scatter(x_data, y_data, color='red', s=80, label='Original Data', zorder=5)

# plot the power law curve (which becomes a straight line on log-log graphs)
plt.plot(x_curve, y_curve, color='blue', label=f'Fit: $y = {a:.2f}x^{{{b:.2f}}}$')

# both axes use logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Customize grid lines for log scales to show major and minor grid lines
plt.grid(True, which="both", linestyle='--', alpha=0.5)

# Axis labels and Title
plt.title('Power Law Fit to VLR Planner Change Data on a Log-Log Scale', fontsize=14)
plt.xlabel('Time (min) [Log Scale]', fontsize=12)
plt.ylabel('Change Rate (%) [Log Scale]', fontsize=12)
plt.legend()

# Save or display the plot
#plt.savefig('log_log_plot.png', bbox_inches='tight')
plt.show()


if (REGULAR_PLOT):
    #### This is what it looks like if you don't use a log-log scale
    plt.scatter(x_data, y_data, color='red', label='Original Data', zorder=5)

    # Create a dense range of x-values to draw a smooth curve
    x_curve = np.linspace(min(x_data) * 0.8, max(x_data) * 1.2, 500)
    y_curve = a * (x_curve ** b)

    # Plot the fitted power law curve
    plt.plot(x_curve, y_curve, color='blue', label=f'Fit: $y = {a:.4f}x^{{{b:.3f}}}$')

    plt.title('Power Law Fit to VLR Planner Change Data')
    plt.xlabel('Time (min)')
    plt.ylabel('Change Rate (%)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()