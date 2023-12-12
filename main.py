def find_and_store_before_ATG(sequence):
    # Find the index of the first occurrence of "ATG" in the sequence
    start_index = sequence.find("ATG")

    if start_index != -1:
        # Extract the sequence before the first occurrence of "ATG"
        sequence_before_ATG = sequence[:start_index]
        return sequence_before_ATG
    else:
        return None

def process_sequences(input_filename, output_filename):
    total_sequences = 0  # Variable to count the total number of sequences

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if line.startswith(">"):
                total_sequences += 1

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        sequence_name = ""
        sequence = ""

        # Write the total number of sequences to the output file
        output_file.write(f"Total sequences in input file: {total_sequences}\n\n")

        for line in input_file:
            if line.startswith(">"):
                if sequence:
                    result = find_and_store_before_ATG(sequence)
                    if result is not None:
                        output_file.write(f">{sequence_name}\n")
                        for i in range(0, len(result), 60):
                            output_file.write(result[i:i+60] + '\n')
                        output_file.write('\n')
                sequence_name = line.strip()[1:]
                sequence = ""  # Start a new sequence
            else:
                sequence += line.strip()  # Append to the current sequence

        # Process the last sequence in the file
        if sequence:
            result = find_and_store_before_ATG(sequence)
            if result is not None:
                output_file.write(f">{sequence_name}\n")
                for i in range(0, len(result), 60):
                    output_file.write(result[i:i+60] + '\n')
                output_file.write('\n')

# Input and output filenames
input_sequences_file = "input.fasta"  # Replace with your input filename
output_file = "output_sequences.fasta"  # Replace with your output filename

# Process sequences and write the results to the output file
process_sequences(input_sequences_file, output_file)
