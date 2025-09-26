# PyTest_003_Shop_App

This project serves as a **learning example of automated testing with Pytest**.  
The goal is to learn the basic principles of testing using a simple shop model.  

The project supports two testing modes:
- **Production shop** – tests functions on a predefined shop.  
- **Custom test shop** – allows you to create your *own shop* just for testing purposes, safely populate it with products, and remove everything after the tests finish.  

This makes it possible to experiment safely and learn how to write tests without affecting production data.

---

## Functionality

The source file [`shop.py`](src/shop/shop.py) contains the following functions:

- `buy(product, qty)` – purchase an item in the production shop, raises `ValueError` if the product does not exist.  
- `on_stock(first_letter: str | None = None)` – returns the number of products in the production shop based on the first letter of the product name, or the total number of products if no letter is provided.  
- helper functions `get(product)`, `add(product, qty)`, `delete(product)` for adding a new product, retrieving the quantity, and deleting a product from the production shop.  
- `buy_test_shop(product, qty, eshop = shop)` – a special function for the **non-production shop**. Used together with the `fix_my_shop` fixture to create and remove test shops, and with the `fill_products` fixture to populate test shops with products.  

---

## Project Structure

```
shop/                            # root directory
│
├─ README.md                     # project documentation (CZ)
├─ README_EN.md                  # project documentation (EN)
├─ pytest.ini                    # pytest configuration
├─ pyproject.toml                # build system (setuptools)
├─ setup.cfg                     # package metadata
│
├─ src/
│   └─ shop/
│       ├─ __init__.py           # import of an object and functions from a source code
│       └─ shop.py               # source code
│
├─ tests/
│   ├─ conftest.py               # fixtures definition
│   ├─ test_shop_buy.py          # tests for buy function (production shop)
│   ├─ test_shop_on_stock.py     # tests for on_stock function (production shop)
│   ├─ test_shop_data.py         # working with the production shop
│   ├─ test_my_shop.py           # working with custom non-production shop
│   ├─ test_exceptions.py        # testing exceptions
│   └─ test_dictionary.py        # examples of how to access keys and values in a dictionary
│
└─ .github/
    └─ workflows/
        └─ ci.yml                # GitHub Actions workflow
```

---

## Installation

Clone the repository and install in *editable* mode:

```bash
git clone https://github.com/<your-username>/pytest-shop-app.git
cd pytest-shop-app
pip install -e .
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_shop_buy.py::test_buy_param
```

Use markers:

```bash
pytest tests/test_shop_buy.py -m positive
pytest tests/test_shop_buy.py -m negative
pytest tests/test_shop_buy.py -m exception
```

---

## ⚙️ CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`).  
It runs tests on Python versions 3.9, 3.10, and 3.11 for every push and pull request.

---

## 📝 License

MIT License – see the [LICENSE](LICENSE) file.
