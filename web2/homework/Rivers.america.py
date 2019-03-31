from mlab import rivers_colection

rivers_america = list(rivers_colection.find({"continent":"S. America"}))

for rivers in rivers_america:
    if rivers["length"] < 1000:
        print(rivers)