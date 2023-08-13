import numpy as np
from scipy import stats

conversion_rates_A = np.array([0.12, 0.22, 0.14, 0.20, 0.17])

conversion_rates_B = np.array([0.1, 0.2, 0.15, 0.25, 0.18])

t_stat, p_value = stats.ttest_ind(conversion_rates_A, conversion_rates_B)

alpha = 0.05  

print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

if p_value < alpha:
    print("There is a statistically significant difference between conversion rates.")
else:
    print("There is no statistically significant difference between conversion rates.")
