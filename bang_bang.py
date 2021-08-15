def shutdown(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'draw'

print(shutdown('Bang!', 'Bang!')) # пробелы перед 'B'