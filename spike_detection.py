Create a Python module that takes the cleaned incident dataframe and computes daily inflow counts.
Add a 7-day rolling average and rolling standard deviation.
Mark a day as a spike when count > rolling average + 2 * std.
Also create category-level and area-level contribution tables for a selected spike day compared with all non-spike days.