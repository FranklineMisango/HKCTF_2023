def decode_ascii_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            ascii_text = f.read()

        decoded_text = ''.join(chr(int(char)) for char in ascii_text.split() if char.isdigit())

        with open(output_file, 'w') as f:
            f.write(decoded_text)

        print("Decoding successful!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_file_path = 'test.txt'
output_file_path = 'output.txt'

decode_ascii_file(input_file_path, output_file_path)