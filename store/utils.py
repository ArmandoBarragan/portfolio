from store.models import Category
def replace_product_attributes(product, new_product):
    product.name = new_product.name
    product.category = new_product.category
    product.price = new_product.price


def save_category(category):
    data = category.cleaned_data
    name = data['name']
    category_to_save = Category(name=name)
    category_to_save.save()
