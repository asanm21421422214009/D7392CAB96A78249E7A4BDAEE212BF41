def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["paint", "boot", "paint", "paint", "sandal", "paint"]
target = "paint"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
