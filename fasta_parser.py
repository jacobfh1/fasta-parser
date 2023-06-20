import csv
from Bio import SeqIO

def fasta_parser(fasta_file):
    sequences = {}

    for record in SeqIO.parse(fasta_file, "fasta"):
        header = record.description.split('|')
        current_name = header[1].strip()
        sequences[current_name] = str(record.seq)

    return sequences

# File name of the input sequence file
input_file = "input.fasta"

# File name of the output TSV file
output_file = "output.tsv"

# Parse the input sequences from the file
sequences = fasta_parser(input_file)

# Generate the sequence statistics
sequence_lengths = [len(seq) for seq in sequences.values()]
total_sequences = len(sequences)
average_length = sum(sequence_lengths) / total_sequences
minimum_length = min(sequence_lengths)
maximum_length = max(sequence_lengths)

# Find the names of sequences with minimum and maximum lengths
sequence_name_min_length = [name for name, length in sequences.items() if len(length) == minimum_length]
sequence_name_max_length = [name for name, length in sequences.items() if len(length) == maximum_length]

# Prepare the data for TSV output
table_data = []
for name, sequence in sequences.items():
    length = len(sequence)
    table_data.append([name, length, sequence])

# Save the output to a TSV file
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["Name", "Length", "Sequence"])
    writer.writerows(table_data)
    writer.writerow([])  # Add an empty row
    writer.writerow(["Sequence Statistics"])
    writer.writerow(["Total Sequences", total_sequences])
    writer.writerow(["Average Length", average_length])
    writer.writerow(["Minimum Length", minimum_length, ", ".join(sequence_name_min_length)])
    writer.writerow(["Maximum Length", maximum_length, ", ".join(sequence_name_max_length)])

# Print the success message
print("Output saved successfully!")