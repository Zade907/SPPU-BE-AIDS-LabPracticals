from collections import Counter
dna = input("Enter a DNA sequence: ").upper().replace(" ", "")
nucleotide_counts = Counter(dna)

def validate(sequence):
    valid_nucleotides = "ATGC"
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False
    return True

if validate(dna):
    print("Nucleotide counts:")
    for nucleotide, count in nucleotide_counts.items():
        print(f"{nucleotide}: {count}")

    #GC Content calculation
    gc_content = (nucleotide_counts['G'] + nucleotide_counts['C']) / len(dna) * 100
    print(f"GC Content: {gc_content:.2f}%")

    motif = input("Enter a motif to search for: ").upper().replace(" ", "")
    #searching for motif in the DNA sequence
    positions = []
    start = 0
    while True:
        position = dna.find(motif, start)

        if position == -1:
            break

        positions.append(position)
        start = position + 1
    if positions:
        print(f"Motif '{motif}' found at positions: {', '.join(map(str, positions))}")
    else:
        print(f"Motif '{motif}' not found in the DNA sequence.")

    #possible coding region 
    #start codon: ATG 
    #stop codons: TAA, TAG, TGA
    found = False 
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    for i in range(len(dna) - 2):

        # Start codon
        if dna[i:i+3] == "ATG":

            # Search for stop codon
            for j in range(i + 3, len(dna) - 2, 3):

                codon = dna[j:j+3]

                if codon in ["TAA", "TAG", "TGA"]:
                    coding_region = dna[i:j+3]

                    print("Start position:", i)
                    print("End position:", j + 2)
                    print("Coding Region:", coding_region)
                    print("Length:", len(coding_region), "bases\n")

                    found = True
                    break

    if not found:
        print("No complete coding region found.")


else:
    print("Invalid DNA sequence. Please enter a sequence containing only A, T, G, and C.")