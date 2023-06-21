# FASTA Parser

This script is designed to perform sequence analysis on FASTA files. It calculates sequence statistics, generates a TSV output file, and provides various functionalities for analyzing protein sequences.

## Features

- Parsing FASTA files to extract sequence data
- Calculating sequence statistics such as total sequences, average length, minimum length, and maximum length
- Saving the analysis results to a tab-separated values (TSV) file
- Identifying sequences with minimum and maximum lengths
- Optional protein domain analysis using InterProScan or Pfam (not implemented)
- Customizable alignment parameters for protein sequences (not implemented)
- Comparison of sequences using pairwise alignment (not implemented)

## Dependencies

The following dependencies are required to run the script:

- Python 3.x
- [Biopython](https://biopython.org/)

Install the dependencies using the following command:

```shell
pip install biopython
```


## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies using the command mentioned above.
3. Prepare a FASTA file containing the input sequences.
4. Update the `input_file` and `output_file` variables in the script with the appropriate file paths.
5. Run the script using the following command:

   ```shell
   python fasta_parser.py

6. The output will be saved in the specified output file as a TSV format, containing the sequence names, lengths, and sequences themselves.
7. You can modify the script parameters and alignment settings as needed for your specific analysis by editing the `fasta_parser.py` file.

## Contributing
Contributions to the project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
