# expense-tracker

Simple CLI tool to track personal expenses.

## Features

- Add expenses with amount, category, and description
- View all expenses in a formatted table
- View total spending
- View spending breakdown by category
- Persistent storage using JSON

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jwe23/expense-tracker.git
cd expense-tracker
```

2. Run the program:
```bash
python expense_tracker.py
```

## Usage

Run the program and follow the menu prompts:
```
--- Expense Tracker ---
1. Add expense
2. View all expenses
3. View total
4. View by category
5. Exit
```

### Example
```
Choice: 1
Amount: $45.50
Category: food
Description: Grocery shopping

✓ Added $45.50 to food
```

## Technologies

- Python 3.x
- JSON for data storage

## Future Improvements

- Delete expenses
- Date range filtering
- Budget warnings
- CSV export
- Data visualization

## License

MIT
