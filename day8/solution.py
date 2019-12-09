layers = []
width = 25
height = 6
pxls_per_layer = 25 * 6

def get_layers():
    layers = []
    pxls_per_layer = 25 * 6
    with open('input.txt', 'r') as f:
        while True:
            cur_layer = []
            for _ in range(pxls_per_layer):
                pixel = f.read(1)
                if not pixel:
                    return layers
                cur_layer.append(pixel)
            layers.append(cur_layer)
        
layers = get_layers()

## Part 1 ##
answer = layers[0]
for layer in layers[1:]:
    if layer.count('0') < answer.count('0'):
        answer = list(layer)
print('PART ONE:')
print(answer.count('1') * answer.count('2'))

## Part 2 ##
result = []
for pixel_idx in range(len(layers[0])):
    for layer in layers:
        pixel = layer[pixel_idx]
        if pixel in ['0', '1']:
            result.append(pixel)
            break

def print_layer(layer: list, width: int, height: int):
    for _ in range(height):
        for _ in range(width):
            c = layer.pop(0)
            print('X' if c == '1' else ' ', end='')
        print('')

print('PART TWO:')
print_layer(result, 25, 6)
