from models.item import Item

url = "https://www.johnlewis.com/2018-apple-ipad-pro-11-inch-a12x-bionic-ios-wi-fi-256gb/p3834478"
tag_name = "p"
query = {"class":"price price--large"}


ipad = Item(url, tag_name, query)
ipad.save_to_mongo()

items_loaded = Item.all()
print(items_loaded[2])
print(items_loaded[2].load_price())