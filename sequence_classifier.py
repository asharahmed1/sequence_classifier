import tkinter as tk
from sklearn.svm import SVC


# Step 1: Read Data from FASTA Format
def read_fasta_file(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            if line.startswith('>'):
                if sequence != "":
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line.strip()
        if sequence != "":
            sequences.append(sequence)
    return sequences


# Step 2: Feature Extraction
def one_hot_encode(sequence):
    encoding = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'U': [0, 0, 0, 1]}
    encoded_sequence = []

    for nucleotide in sequence:
        encoded_sequence.extend(encoding.get(nucleotide, [0, 0, 0, 0]))

    feature_length = 31 * 4  # Assuming a maximum sequence length of 31

    if len(encoded_sequence) < feature_length:
        encoded_sequence += [0] * (feature_length - len(encoded_sequence))
    elif len(encoded_sequence) > feature_length:
        encoded_sequence = encoded_sequence[:feature_length]

    return encoded_sequence


# Step 3: Train a Machine Learning Model
positives_file = "Positive_train.txt"
negatives_file = "Negatives_train.txt"

positive_sequences = read_fasta_file(positives_file)
negative_sequences = read_fasta_file(negatives_file)

# Combine the positive and negative sequences into a single dataset
sequences = positive_sequences + negative_sequences

# Create labels for the sequences
labels = [1] * len(positive_sequences) + [0] * len(negative_sequences)

# Perform feature extraction
features = [one_hot_encode(sequence) for sequence in sequences]

# Train the SVM model
svm = SVC(probability=True)
svm.fit(features, labels)


# Step 4: Develop GUI
def classify_sequence():
    sequence = sequence_entry.get()
    sequence_type = determine_sequence_type(sequence)

    encoded_sequence = one_hot_encode(sequence)
    result = svm.predict([encoded_sequence])
    probability = svm.predict_proba([encoded_sequence])[0][result[0]]

    result_label.config(text=f"Classification: {'Positive' if result[0] == 1 else 'Negative'}")
    probability_label.config(text=f"Probability: {probability:.4f}")
    type_label.config(text=f"Type: {sequence_type}")


def determine_sequence_type(sequence):
    dna_letters = set('ACGT')
    rna_letters = set('ACGU')
    protein_letters = set('ACDEFGHIKLMNPQRSTVWY')

    sequence_set = set(sequence.upper())

    if sequence_set.issubset(dna_letters):
        return "DNA"
    elif sequence_set.issubset(rna_letters):
        return "RNA"
    elif sequence_set.issubset(protein_letters):
        return "Protein"
    else:
        return "Unknown"


# Create a GUI window
window = tk.Tk()
window.title("Sequence Classification Model developed by Ashar")

# Create GUI elements
sequence_label = tk.Label(window, text="Enter sequence:")
sequence_label.pack()

sequence_entry = tk.Entry(window, width=50)
sequence_entry.pack()

classify_button = tk.Button(window, text="Classify", command=classify_sequence)
classify_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

probability_label = tk.Label(window, text="")
probability_label.pack()

type_label = tk.Label(window, text="")
type_label.pack()

# Sample input sequences for testing
sample_sequences = [
    "ATCGATCGATCG",  # DNA sequence
    "AUUUGCAUCGUA",  # RNA sequence
    "MKLWEKMNKELK",  # Protein sequence
    "AGCTUAGC"  # Unknown sequence
]

for sequence in sample_sequences:
    print(f"Sequence: {sequence}")
    sequence_type = determine_sequence_type(sequence)
    encoded_sequence = one_hot_encode(sequence)
    result = svm.predict([encoded_sequence])
    probability = svm.predict_proba([encoded_sequence])[0][result[0]]
    print(f"Classification: {'Positive' if result[0] == 1 else 'Negative'}")
    print(f"Probability: {probability:.4f}")
    print(f"Type: {sequence_type}")
    print()

# Run the GUI loop
window.mainloop()
