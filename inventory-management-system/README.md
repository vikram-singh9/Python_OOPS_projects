# Streamlit Inventory Management System

A modern, user-friendly inventory management system built with Python, Streamlit, and SQLAlchemy. This application provides a web-based interface for managing product inventory, including features for adding, updating, viewing, and deleting products.

## Features

- View complete inventory with sorting and filtering capabilities
- Add new products with details (name, quantity, price, category)
- Update existing product information
- Delete products from inventory
- Persistent storage using SQLite database
- Clean and intuitive user interface

## Requirements

- Python 3.8 or higher
- Streamlit
- SQLAlchemy
- Pandas
- python-dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd inventory-management-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar menu to navigate between different functions:
   - View Inventory: Display all products in a sortable table
   - Add Product: Create new product entries
   - Update Product: Modify existing product information
   - Delete Product: Remove products from inventory

## Project Structure

```
inventory-management-system/
├── main.py              # Main application file with UI and business logic
├── pyproject.toml       # Project dependencies and metadata
├── README.md           # Project documentation
└── inventory.db        # SQLite database (created on first run)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.