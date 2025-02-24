import tkinter as tk
from tkinter import ttk
import logging
from functools import wraps
from typing import Any

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_call(func: Any) -> Any:
    """Decorator to log function calls and their results."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Calling %s with args=%s kwargs=%s", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        logging.info("%s returned %s", func.__name__, result)
        return result
    return wrapper

class CompoundInterestCalculator(tk.Tk):
    """A GUI application for calculating compound interest."""
    
    def __init__(self) -> None:
        super().__init__()
        self.title("Compound Interest Calculator")
        self.configure_gui()
        self.create_widgets()
        
    def configure_gui(self) -> None:
        """Configure main window settings."""
        self.geometry("400x250")
        self.resizable(False, False)
        
    def create_widgets(self) -> None:
        """Create and place all widgets on the window."""
        # Principal Amount
        self.principal_label = tk.Label(self, text="Principal Amount:")
        self.principal_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.principal_var = tk.DoubleVar(value=1000.0)
        self.principal_entry = tk.Entry(self, textvariable=self.principal_var)
        self.principal_entry.grid(row=0, column=1, padx=5, pady=5)

        # Interest Rate Slider
        self.rate_label = tk.Label(self, text="Interest Rate (%):")
        self.rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rate_var = tk.DoubleVar(value=5.0)
        self.rate_slider = tk.Scale(self, from_=0, to=20, orient=tk.HORIZONTAL, variable=self.rate_var)
        self.rate_slider.grid(row=1, column=1, padx=5, pady=5)

        # Number of Years Slider
        self.years_label = tk.Label(self, text="Number of Years:")
        self.years_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.years_var = tk.DoubleVar(value=10.0)
        self.years_slider = tk.Scale(self, from_=0, to=30, orient=tk.HORIZONTAL, variable=self.years_var)
        self.years_slider.grid(row=2, column=1, padx=5, pady=5)

        # Compound Frequency
        self.compound_label = tk.Label(self, text="Compound Frequency:")
        self.compound_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.compound_var = tk.IntVar(value=12)
        self.compound_entry = tk.Entry(self, textvariable=self.compound_var)
        self.compound_entry.grid(row=3, column=1, padx=5, pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_compound_interest)
        self.calculate_button.grid(row=4, column=0, padx=5, pady=10)

        # Result Display
        self.result_var = tk.StringVar(value="Future Value: N/A")
        self.result_label = tk.Label(self, textvariable=self.result_var, font=("Helvetica", 12))
        self.result_label.grid(row=4, column=1, padx=5, pady=10)
        
    @log_call
    def calculate_compound_interest(self) -> None:
        """
        Calculate the future value using the compound interest formula:
        Future Value = Principal * (1 + (rate/compound_frequency))^(compound_frequency * years)
        """
        try:
            principal = self.principal_var.get()
            rate = self.rate_var.get() / 100.0  # Convert percentage to decimal
            years = self.years_var.get()
            compound_freq = self.compound_var.get()
            
            future_value = principal * (1 + (rate / compound_freq)) ** (compound_freq * years)
            self.result_var.set(f"Future Value: ${future_value:.2f}")
        except Exception as e:
            logging.error("Error calculating compound interest", exc_info=True)
            self.result_var.set("Error computing value.")

if __name__ == '__main__':
    app = CompoundInterestCalculator()
    app.mainloop()
