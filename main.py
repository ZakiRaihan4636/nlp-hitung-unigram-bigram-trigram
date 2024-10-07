# Teks yang akan dianalisis
text = """Jalan jalan ke rumah mpok Atun. Rumah mpok Atun, ada di samping rumah bang Mandra.
Tugas ketiga kita suruh nyari pantun. Yuk kita kumpulkan di Elena segera coba ini."""

# Langkah 1: Tokenisasi (memisahkan kata-kata)
tokens = text.replace(".", "").replace(",", "").lower().split()

# Inisialisasi dictionary untuk menyimpan frekuensi
unigram_freq = {}
bigram_freq = {}
trigram_freq = {}

# Langkah 2: Menghitung frekuensi unigram, bigram, dan trigram
for i in range(len(tokens)):
    # Menghitung unigram
    word = tokens[i]
    if word in unigram_freq:
        unigram_freq[word] += 1
    else:
        unigram_freq[word] = 1

    # Menghitung bigram
    if i < len(tokens) - 1:
        bigram = (tokens[i], tokens[i + 1])
        if bigram in bigram_freq:
            bigram_freq[bigram] += 1
        else:
            bigram_freq[bigram] = 1

    # Menghitung trigram
    if i < len(tokens) - 2:
        trigram = (tokens[i], tokens[i + 1], tokens[i + 2])
        if trigram in trigram_freq:
            trigram_freq[trigram] += 1
        else:
            trigram_freq[trigram] = 1

# Langkah 3: Menampilkan hasil
print("Unigram:")
for word, freq in unigram_freq.items():
    print(f"{word}: {freq}")

print("\nBigram:")
for bigram, freq in bigram_freq.items():
    print(f"{bigram}: {freq}")

print("\nTrigram:")
for trigram, freq in trigram_freq.items():
    print(f"{trigram}: {freq}")
