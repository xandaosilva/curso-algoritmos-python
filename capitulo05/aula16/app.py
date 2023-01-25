product_a, product_b, product_c = ["Blender", "white", 100], ["Bed", "brown", 550], ["T-shirt", "yellow", 250]
product_d, product_e, product_f = ["Air Friyer", "black", 300], ["Sneakers", "blue", 180], ["Pressure cooker", "black", 350]
product_g, product_h, product_i = ["Schoolbag", "Green", 70], ["Gloves", "black", 30], ["Wardrobe", "white", 400]
product_j = ["Lampshade", "white", 130]

list_products = [product_a, product_b, product_c, product_d, product_e, product_f, product_g, product_h, product_i, product_j]

for product in list_products:
    print(f"Product: {product[0]} - Color: {product[1]} - Price: ${product[2]:.2f}")

