import os
from .huffman.frequency import read_file_and_count_frequencies
from .huffman.tree import build_huffman_tree
from .huffman.codes import generate_huffman_codes
from .huffman.encoder import encode_text, pad_bitstring, write_compressed_file
from .huffman.decoder import read_compressed_file, remove_padding, decode_text

def compress(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    freq_table = read_file_and_count_frequencies(input_file_path)
    huffman_tree = build_huffman_tree(freq_table)
    code_table = generate_huffman_codes(huffman_tree)

    encoded_data = encode_text(text, code_table)

    output_path = input_file_path + '.huff'
    write_compressed_file(output_path, freq_table, encoded_data)

    return output_path


def decompress(input_file_path):
    freq_table, bitstring = read_compressed_file(input_file_path)
    unpadded_bitstring = remove_padding(bitstring)
    huffman_tree = build_huffman_tree(freq_table)
    decoded_text = decode_text(unpadded_bitstring, huffman_tree)

    output_file = input_file_path.replace('.huff', '.decompressed.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_text)

    return output_file
