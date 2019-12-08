from sys import stdout


def split_layers(digit_string, height, width):
    size = height * width
    layers = []
    for i in range(0, len(digit_string), size):
        layers.append(digit_string[i:i + size])

    return layers


def combine_layers(layers, height, width):
    result = []
    for pixel_idx in range(height * width):
        for layer in layers:
            if layer[pixel_idx] != '2':
                result.append(layer[pixel_idx])
                break

    return ''.join(result)


def render_image(flat_image, height, width):
    rendered_image = ''
    for idx in range(0, len(flat_image), width):
        rendered_image += flat_image[idx:idx + width] + '\n'

    return rendered_image.replace('0', ' ').replace('1', '#')


def solve_part_1(puzzle_input):
    layers = split_layers(puzzle_input.strip(), 6, 25)

    min_0_layer = layers[0]
    min_0 = layers[0].count('0')
    for layer in layers[1:]:
        num_0 = layer.count('0')
        if num_0 < min_0:
            min_0 = num_0
            min_0_layer = layer

    return min_0_layer.count('1') * min_0_layer.count('2')


def solve_part_2(puzzle_input):
    layers = split_layers(puzzle_input, 6, 25)
    flat_image = combine_layers(layers, 6, 25)
    return render_image(flat_image, 6, 25)
