from mlab import rivers_colection

rivers_afica = list(rivers_colection.find({"continent":"Africa"}))
print(rivers_afica)
