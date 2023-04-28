def process_duplicates(input_file_descriptor, output_file_descriptor):
    operation_index = 0
    last = None
    for line in input_file_descriptor:
        number = line.strip()

        if operation_index == 0:
            operation_index += 1
            continue
        if number != last:
            last = number
            output_file_descriptor.write(f"{number}\n")


input_file = open('./input.txt', 'r')
output_file = open('./output.txt', 'w')
process_duplicates(input_file, output_file)
output_file.close()

