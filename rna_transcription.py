def to_rna(dna_strand):
    # convert string to list
    # run each item in the new list through the dictionary to transcribe
    # convert the transcribed list back into a string
    # return the new string

    # Transcription dictionary: the key is the DNA letter, the RNA is the value
    transcription = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    broken = list(dna_strand) # convert string to list
    transcribed = [] #initialize the list

    for dna in broken:
        transcribed.append(transcription[dna])

    return ("".join(transcribed))

if __name__ == '__main__':
    to_rna("GC")
