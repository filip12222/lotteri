import random

class lotteri:

    def __init__(self):

        self.list_vinster = [
        "Solstol", 
        "Iphone",
        "Handduk",
        "Tandborste",
        "Ockelbo 500",
        "Polaris RMK",
        "BMX",
        "Lyx yatch",
        "El sparkcykel",
        "Skateboard",
        "Hawai resa",
        "Kaffe och Bulle",
        "Jbl hörlurar",
        "Konsert med Queen",
        "ICA matkasse",
        "Surfbräda",
        "Ficklampa",
        "Bregott",
        "Tugummi",
        "2L Tvål"
        ]

    def get_vinst(self):
        slumptal = random.randint(0,19)
        return self.list_vinster[slumptal]
