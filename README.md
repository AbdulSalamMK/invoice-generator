# 🧾 Invoice Generator (Python)

This is a beginner-friendly Python script that helps small business owners generate professional **PDF invoices**.

---

## 🚀 Features

- Accepts **customer name**, **invoice date**, and **items** (name, quantity, price)
- Calculates item-wise and grand totals
- Generates a clean **PDF invoice**
- Saves with a **unique filename** (e.g., `invoice_John_Doe_20250507123456.pdf`)

---

## 🛠️ How to Use

### 1. Install Python

Download from: https://www.python.org/downloads/

### 2. Install Required Library

```bash
pip install fpdf
```

### 3. Run the Script

```bash
python invoice_generator.py
```

Edit the customer and item list inside the script to generate a new invoice.

---

## 🧾 Example Item Format

```python
customer = "John Doe"
items = [
    ("Product A", 2, 50.00),
    ("Product B", 1, 30.00),
    ("Product C", 3, 20.00)
]
```

---

## 📄 Output

Creates a PDF file like:
```
invoice_John_Doe_20250507123456.pdf
```

---

## 🙋‍♂️ Created By

**Fawaz** – Python Freelancer  
Need help or customizations? Contact me!

---

## 📄 License

Free and open-source. Use it however you like!
