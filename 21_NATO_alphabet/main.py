import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_rows = data.iterrows()
alphabet_dict = {row.letter: row.code for (index, row) in data_rows}
word = input('Enter any word to generate a list of the phonetic code words:\n').upper()

result = [alphabet_dict[letter] for letter in word]
print(result)
