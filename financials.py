import pandas as pd
import numpy as np

def simple_projection_table(months: int = 12, base_users: int = 100, monthly_growth: float = 0.15, arpu: float = 5.0, cogs_pct: float = 0.25, opex: float = 2000.0):
    """
    Very simple top-line projection model:
    - Users grow by monthly_growth
    - Revenue = Users * ARPU
    - COGS = Revenue * cogs_pct
    - Gross Profit = Revenue - COGS
    - OPEX = fixed monthly cost
    - Net Profit = Gross Profit - OPEX
    """
    data = []
    users = base_users
    for m in range(1, months+1):
        revenue = users * arpu
        cogs = revenue * cogs_pct
        gross = revenue - cogs
        net = gross - opex
        data.append({
            "Month": m,
            "Users": int(round(users)),
            "Revenue": round(revenue, 2),
            "COGS": round(cogs, 2),
            "Gross Profit": round(gross, 2),
            "OPEX (Fixed)": round(opex, 2),
            "Net Profit": round(net, 2),
        })
        users *= (1 + monthly_growth)
    df = pd.DataFrame(data)
    return df
