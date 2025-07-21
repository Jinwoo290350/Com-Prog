def count_differences(word1, word2):
    differences = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differences += 1
    return differences

def can_chain(word1, word2):
    return count_differences(word1, word2) <= 2

text = input("Text: ")
words = text.split()

used = [False] * len(words)
chains = []

i = 0
while i < len(words):
    if used[i]:
        i += 1
        continue
    
    current_chain = [words[i]]
    used[i] = True
    current_word = words[i]
    
    j = i + 1
    while j < len(words):
        if not used[j] and can_chain(current_word, words[j]):
            current_chain.append(words[j])
            used[j] = True
            current_word = words[j]
            j = 0
        else:
            j += 1
    
    chains.append(current_chain)
    i += 1

num_chains = len(chains)
max_length = max(len(chain) for chain in chains) if chains else 0

print(f"{num_chains} Chain(s). Maximum length is {max_length} word(s).")