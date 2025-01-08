def introspection_info(obj):
    attributes = []
    methods = []
    for i in dir(obj):
        if not i.startswith("__"):
            attributes.append(i)
        else:
            methods.append(i)

    book = {
        'type': type(obj).__name__,
        'attributes': attributes,
        'methods': methods,
        'module': getattr(obj, '__module__', None)
    }
    return book


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
