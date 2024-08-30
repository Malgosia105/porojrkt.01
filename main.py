meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "CREEPY": "straszny, złowieszczy",
}
while True:
    
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("niestety tego słowa nie ma w naszym słowniku.")
