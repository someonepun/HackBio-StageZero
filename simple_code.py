#Print Team info
team_aspartic = [
    {
        "name": "Niraj Pun Magar",
        "slack_username": "@Niraj Pun Magar ",
        "country": "Nepal",
        "hobby": "Product Design",
        "affiliation": "Kathmandu University",
        "favorite_gene": ">NC_060943.1:47730492-47734089 APOE [organism=Homo sapiens] [GeneID=348] [chromosome=19]CTACTCAGCCCCAGCGGAGGTGAAGGACGTCCTTCCCCAGGAGCCGGTGAGAAGCGCAGTCGGGGGCACGGGGATGAGCTCAGGGGCCTCTAGAAAGAGCTGGGACCCTGGGAAGCCCTGGCCTCCAGGTAGTCTCAGGAGAGCTACTCGGGGTCGGGCTTGGGGAGAGGAGGAGCGGGGGTGAGGCAAGCAGCAGGGGACTGGACCTGGGAAGGGCTGGGCAGCAGAGACGACCCGACCCGCTAGAAGGTGGGGTGGGGAGAGCAGCTGGACTGGGATG"
    }
]

def print_info():
    for member in team_aspartic:
        print("Team Member Information:")
        print(f"Name: {member['name']}")
        print(f"Slack Username: {member['slack_username']}")
        print(f"Country: {member['country']}")
        print(f"Hobby: {member['hobby']}")
        print(f"Affiliation: {member['affiliation']}")
        print(f"Favorite Gene Sequence: {member['favorite_gene']}")

print_info()
    

 
#DNA to PROTEIN
def translate_dna(dna_seq: str, frame: int = 1, to_stop: bool = False) -> str:
    codon_table = {
        # Phenylalanine, Leucine
        "TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L",
        # Isoleucine, Methionine
        "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
        # Valine
        "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
        # Serine
        "TCT":"S","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S",
        # Proline
        "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
        # Threonine
        "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
        # Alanine
        "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
        # Tyrosine, Stop
        "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
        # Histidine, Glutamine
        "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
        # Asparagine, Lysine
        "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
        # Aspartic acid, Glutamic acid
        "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
        # Cysteine, Tryptophan, Stop
        "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
        # Arginine
        "CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
        # Glycine
        "GGT":"G","GGC":"G","GGA":"G","GGG":"G",
    }

    # remve header, whitespace, and convertion of U to T
    lines = dna_seq.strip().splitlines()
    if lines and lines[0].startswith(">"):
        lines = lines[1:]
    seq = "".join(lines).replace(" ", "").replace("\t", "").upper().replace("U", "T")

    if frame not in (1, 2, 3):
        raise ValueError("f must be 1, 2, or 3")

    start = frame - 1
    aa_list = []
    for i in range(start, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if len(codon) < 3:
            break
        aa = codon_table.get(codon, "X")
        if aa == "*" and to_stop:
            break
        aa_list.append(aa)

    return "".join(aa_list)


#Distance calculate
def hamming_distance(slack_username: str, twitter_handle: str) -> int:
        max_length = max(len(slack_username), len(twitter_handle))
        slack_username = slack_username.ljust(max_length, ' ')
        twitter_handle = twitter_handle.ljust(max_length, ' ')

        distance = sum(1 for a, b in zip(slack_username, twitter_handle) if a != b)
        return distance

slack_username = "@Niraj Pun Magar"
twitter_handle = "NirajP"
distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming Distnce: {distance}")