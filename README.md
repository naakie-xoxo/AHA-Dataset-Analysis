# STAT440: AHA Hospital Data Analysis

## Quick Start (4 Steps)
1. **Clone the repo:**
   `git clone <your-repo-url>`
2. **Install required libraries** (run this in your terminal):
   `pip install -r requirements.txt`
3. **Open your assigned notebook** in `/notebooks/` and click **Select Kernel** (top right in VS Code) to pick your Python environment.
4. **Run Cell 1:** The dataset is already cleaned and pre-loaded for you.

## Saving Your Outputs
- **Charts:** Save to `outputs/figures/` as `.png` files:
  `plt.savefig('../outputs/figures/your_chart_name.png', dpi=300, bbox_inches='tight')`
- **Summary Tables:** Save to `outputs/tables/` as `.csv` files:
  `your_table.to_csv('../outputs/tables/your_table_name.csv', index=False)`

## Team Rules
- **Do not** edit `data/processed/aha_cleaned.csv` or anyone else's notebook.
- Always run `git pull` before you start working and before you push.
- When you finish a section, push your changes:
  ```bash
  git add .
  git commit -m "Completed Role X analysis"
  git push