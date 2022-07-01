def name(h,g, *args, key):#h-позиционный параметр/ все остальные в *args - кортеж параметр *args/ key-ключевой параметр
    print(h)
    print(g)
    print(args)
    print(key)

name (7, 0, 8, 5, key=10)