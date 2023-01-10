# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:29:33 2023

@author: timot
"""

import tkinter as tk
from tkinter import ttk

class CompoundInterestCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Compound Interest Calculator")

        self.principal_label = tk.Label(self, text="Principal Amount:")
        self.principal_label.grid(row=0, column=0, padx=5, pady=5)
        self.principal_var = tk.DoubleVar(value=1000)
        self.principal_entry = tk.Entry(self, textvariable=self.principal_var)
        self.principal_entry.grid(row=0, column=1, padx=5, pady=5)

        self.rate_label = tk.Label(self, text="Interest Rate (%):")
        self.rate_label.grid(row=1, column=0, padx=5, pady=5)
        self.rate_var = tk.DoubleVar(value=5)
        self.rate_slider = tk.Scale(self, from_=0, to=20, orient='horizontal', variable=self.rate_var)
        self.rate_slider.grid(row=1, column=1, padx=5, pady=5)

        self.years_label = tk.Label(self, text="Number of Years:")
        self.years_label.grid(row=2, column=0, padx=5, pady=5)
        self.years_var = tk.DoubleVar(value=10)
        self.years_slider = tk.Scale(self, from_=0, to=30, orient='horizontal', variable=self.years_var)
        self.years_slider.grid(row=2, column=1, padx=5, pady=5)

        self.compound_label = tk.Label(self, text="Compound Frequency:")
        self.compound_label.grid(row=3, column=0, padx=5, pady=5)
        self.compound_var = tk.IntVar(value=12)
        self.compound_entry = tk.Entry(self, textvariable=self.compound_var)
        self.compound_entry.grid(row=3, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(self, text="Calculate", command

        def calculate_compound_interest(self):
        principal = self.principal_var.get()
        rate = self.rate_var.get()/100
        years = self.years_var.get()
        compounding_frequency = self.compound_var.get()

        future_value = principal * (1 + (rate / compounding_frequency)) ** (compounding_frequency * years)

        self.result_var.set("Future Value: ${:.2f}".format(future_value))

    def __init__(self):
        super().__init__()
        self.title("Compound Interest Calculator")

        # rest of the code

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_compound_interest)
        self.calculate_button.grid(row=4, column=0, padx=5, pady=5)

        self.result_var = tk.StringVar(value="N/A")
        self.result = tk.Label(self, textvariable=self.result_var)
        self.result.grid(row=4, column=1, padx=5, pady=5)


if __name__ == '__main__':
    calculator = CompoundInterestCalculator()
    calculator.mainloop()
