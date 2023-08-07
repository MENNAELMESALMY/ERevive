def convertToCamelCase(s):
    return ''.join(x.capitalize() if i!=0 else x.lower() for i,x in enumerate(s.split('_')))

