def read_byte_file(filename):
    matrix = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('.byte'):
                continue
            
            # Remove ".byte" and split values
            values = line.replace('.byte', '').strip()
            values = values.split(',')
            values = [v.strip() for v in values if v.strip()]
            
            matrix.append(values)
    
    return matrix


def write_byte_file(filename, matrix):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write('.byte ' + ','.join(row) + '\n')


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


# ===== MAIN =====
input_file = "input.txt"
output_file = "output.txt"

matrix = read_byte_file(input_file)

# Optional safety check
print(f"Original size: {len(matrix)} rows x {len(matrix[0])} columns")

transposed = transpose_matrix(matrix)

print(f"Transposed size: {len(transposed)} rows x {len(transposed[0])} columns")

write_byte_file(output_file, transposed)

print("Done!")
