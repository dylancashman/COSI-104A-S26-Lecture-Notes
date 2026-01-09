"""
COSI 104A - Introduction to Machine Learning
Brandeis University
Linear Regression Parameter Visualization

This Python script creates an interactive applet to demonstrate the effect of the slope parameter
in a simple linear regression model. It visualizes the regression line and the corresponding
mean squared error (MSE) loss surface.

Created with assistance from Google's Gemini.

Author: Dylan Cashman (dylancashman@brandeis.edu)
Date: March 20, 2025
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def create_regression_app():
    """Creates a simple regression applet with two graphs and a slider."""

    root = tk.Tk()
    root.title("Linear Regression Parameter Demo")

    # Generate some sample data
    np.random.seed(42)  # For reproducibility
    x = np.linspace(0, 10, 10)
    true_slope = 2
    y = true_slope * x + np.random.normal(0, 5, 10) # add noise

    # Create the left graph (scatter plot with regression line)
    fig_scatter, ax_scatter = plt.subplots(figsize=(2.5, 2))
    ax_scatter.scatter(x, y)
    ax_scatter.set_xlabel("X")
    ax_scatter.set_ylabel("Y")
    ax_scatter.set_title("Data and Regression Line")
    canvas_scatter = FigureCanvasTkAgg(fig_scatter, master=root)
    canvas_scatter.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

    # Create the right graph (loss surface)
    fig_loss, ax_loss = plt.subplots(figsize=(2.5, 2))
    ax_loss.set_xlabel("Slope")
    ax_loss.set_ylabel("Mean Squared Error")
    ax_loss.set_title("Loss Surface")
    canvas_loss = FigureCanvasTkAgg(fig_loss, master=root)
    canvas_loss.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

    # Create the slider
    slider_label = ttk.Label(root, text="Slope:")
    slider_label.grid(row=1, column=0, columnspan=2, pady=(5, 0))
    slope_slider = ttk.Scale(root, from_=-2, to=4, orient=tk.HORIZONTAL, length=200)
    slope_slider.set(1)  # Initial slope value
    slope_slider.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10))

    def update_graphs(slope):
        """Updates the graphs based on the slider value."""
        slope = slope_slider.get() #get the current value of the slider.

        # Update the scatter plot
        ax_scatter.clear()
        ax_scatter.scatter(x, y)
        ax_scatter.plot(x, slope * x, color='red') #regression line.
        ax_scatter.set_xlabel("X")
        ax_scatter.set_ylabel("Y")
        ax_scatter.set_title("Data and Regression Line")
        canvas_scatter.draw()

        # Calculate and update the loss surface
        slopes = np.linspace(-2, 4, 100)
        mse_values = []
        for s in slopes:
            y_pred = s * x
            mse = np.mean((y - y_pred)**2)
            mse_values.append(mse)

        ax_loss.clear()
        ax_loss.plot(slopes, mse_values)
        ax_loss.scatter(slope, np.mean((y-slope*x)**2), color = 'red') #mark the current mse.
        ax_loss.set_xlabel("Slope")
        ax_loss.set_ylabel("Mean Squared Error")
        ax_loss.set_title("Loss Surface")
        canvas_loss.draw()

    # Bind the slider to the update function
    slope_slider.config(command=lambda _: update_graphs(slope_slider.get()))

    # Initial update
    update_graphs(slope_slider.get())

    root.mainloop()

if __name__ == "__main__":
    create_regression_app()