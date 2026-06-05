# 📂 csv-structure-comparator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> A utility to validate structural consistency between two CSV files — detecting missing or extra columns compared to a reference file.

---

## 📌 Description

In data pipelines, it is common to receive CSV files from external sources that are expected to follow a predefined structure. **csv-structure-comparator** compares the column sets of two CSV files and reports:

- ✅ Whether the structure is identical
- ❌ Which columns are **missing** in the new file
- ➕ Which columns were **added** unexpectedly

---

## 🗂️ Project Structure

```
csv-structure-comparator/
├── compare_csv_structure.py   # Main script
├── data/
│   ├── dados_modelo.csv       # Reference file (expected structure)
│   └── dados_recebidos.csv    # Received file to be validated
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/csv-structure-comparator.git
cd csv-structure-comparator
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```python
from compare_csv_structure import compare_csv_structure

compare_csv_structure('data/dados_modelo.csv', 'data/dados_recebidos.csv')
```

Or run directly from the terminal:

```bash
python compare_csv_structure.py
```

---

## 📋 Output Examples

**When both files have the same structure:**

```
✅ Success: The CSV file structure is exactly the same.
```

**When divergences are found:**

```
⚠️ Warning: Structural divergences were found!
❌ Columns missing in the new file: {'unit_price', 'due_date'}
➕ New columns that were added: {'applied_discount'}
```

---

## 📦 Dependencies

```
pandas>=2.0.0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Made by **Rafael** — [github.com/rafaeloureiro](https://github.com/rafaeloureiro)
