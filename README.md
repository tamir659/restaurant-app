# Restaurant Ordering App

A full-stack restaurant ordering web app built with **Flask** and **SQLAlchemy**.
Customers browse the menu, fill a cart and place delivery orders; staff manage the menu and
track orders from a separate dashboard.

## Features

**Customers**
- Sign up / log in, edit account details
- Browse menu by category, view dish details (vegetarian / gluten-free flags)
- Shopping cart: add and remove items
- Place a delivery order and view order history

**Staff**
- Separate staff login
- Add, edit and delete categories and dishes
- View incoming orders and mark them as delivered

## Tech stack

- Python, Flask (Blueprints), Jinja2 templates
- Flask-SQLAlchemy ORM — SQLite locally, PostgreSQL in deployment
- Flask-WTF / WTForms for form validation
- Docker

## Project structure

```
server.py        # app setup, DB config, blueprint registration
db.py            # SQLAlchemy instance
models/          # User, Category, Dish, Cart, Items, Delivery
routes/site.py   # customer-facing routes
routes/staff.py  # staff dashboard routes
forms.py         # WTForms form classes
utils.py         # auth helpers
templates/       # Jinja2 templates (site/ and staff/)
static/          # CSS and images
seed.py          # sample categories and dishes
```

## Running locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python seed.py                 # optional: load sample menu data
python server.py
```

Then open http://127.0.0.1:5000

### Configuration

| Variable       | Default                    | Purpose                         |
|----------------|----------------------------|---------------------------------|
| `DATABASE_URL` | `sqlite:///restaurant.db`  | Any SQLAlchemy URL (e.g. Postgres) |
| `SECRET_KEY`   | dev-only value             | Flask session / CSRF secret     |

### Docker

```bash
docker build -t restaurant-app .
docker run -p 5000:5000 -e SECRET_KEY=your-secret restaurant-app
```
