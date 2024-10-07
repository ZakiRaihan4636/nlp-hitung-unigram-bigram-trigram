# Teks pantun yang akan dianalisis
text = """Surya tenggelam ke barat
Senja hati merah cahayanya
Jika ingin dapat dunia akhirat
Ilmu dan amal adalah kuncinya
Kalau mau makan sukun
Jangan lupa makan kedondong
Kalau mau hidup rukun
Jangan lupa tolong-menolong
Merah muda baju si Bibi
Di tangan ada bayam seikat
Masalah warga datang bertubi-tubi
Berkumpullah untuk mufakat
Setelah makan menggosok gigi
Gigi bersih nan putih pula
Janganlah pelit untuk berbagi
Membantu sesama bonus pahala
Berbelanja ke Bu Satunah
Buka pagi sampai malam
Janganlah suka memfitnah
Fitnah itu amat kejam
Buah duku buah kedondong
Enak rasanya dimakan bersama
Jika engkau suka berbohong
Sedih hati ayah dan bunda
Ikan nila dimakan berang-berang
Katak hijau melompat ke kiri
Jika berada di rantau orang
Baik-baik membawa diri"""

# Langkah 1: Tokenisasi (memisahkan kata-kata)
tokens = text.replace("\n", " ").replace(",", "").replace(".", "").lower().split()

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
