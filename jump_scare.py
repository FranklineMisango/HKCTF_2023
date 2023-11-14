def checker(code):
    if ';' in code: return False
    for line in code.split('\n'):
        if not line.startswith('JMP '): return False
    return True
