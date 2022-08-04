import argparse


def mutagenize(sequence):
	sequence_listing = list(sequence)
	amino_acid_list = ["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]

	pos = 0
	probabilities = []

	while pos < len(sequence):


		for amino in amino_acid_list:


			q = list(sequence)
		
			if amino != sequence[pos]:
			
				q[pos] = amino
				s ="".join(q)
				

				probabilities.append(s)


		
		pos +=1

	return (print(probabilities))



def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="")

    parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Run the program in verbose mode.")
    
    parser.add_argument("mutagenize_sequence")
    
    options = parser.parse_args()
    return options








if __name__ == "__main__":

	options = getArguments()

	sequence_to_mutagenize = options.mutagenize_sequence



	mutagenize(sequence_to_mutagenize)











