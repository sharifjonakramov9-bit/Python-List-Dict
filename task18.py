def group_products_by_category(products: list[dict]) -> dict[str, list[dict]]:
    n = {}

    for i in products:
        n.setdefault(i["category"], []).append(i)

    return n

products = [
    {"name": "iPhone 15", "price": 1200, "category": "Electronics"},
    {"name": "Samsung TV", "price": 800, "category": "Electronics"},
    {"name": "Nike Shoes", "price": 150, "category": "Fashion"},
    {"name": "Adidas Shoes", "price": 120, "category": "Fashion"},
    {"name": "Couch", "price": 500, "category": "Furniture"},
    {"name": "Chair", "price": 100, "category": "Furniture"},
    {"name": "MacBook Pro", "price": 2000, "category": "Electronics"},
    {"name": "T-shirt", "price": 25, "category": "Fashion"},
    {"name": "Desk", "price": 220, "category": "Furniture"},
    {"name": "Monitor", "price": 300, "category": "Electronics"},
    {"name": "Keyboard", "price": 50, "category": "Electronics"},
    {"name": "Mouse", "price": 30, "category": "Electronics"},
    {"name": "Jeans", "price": 80, "category": "Fashion"},
    {"name": "Jacket", "price": 200, "category": "Fashion"},
    {"name": "Bed", "price": 700, "category": "Furniture"},
    {"name": "Lamp", "price": 60, "category": "Furniture"},
    {"name": "iPad", "price": 900, "category": "Electronics"},
    {"name": "Watch", "price": 250, "category": "Fashion"},
    {"name": "Bookshelf", "price": 400, "category": "Furniture"},
    {"name": "Headphones", "price": 180, "category": "Electronics"},
]

idk = group_products_by_category(products)
print(idk)
