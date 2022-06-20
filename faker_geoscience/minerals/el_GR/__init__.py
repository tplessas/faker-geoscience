from .. import Provider as MineralsProvider


class Provider(MineralsProvider):
    gemstone_names = (
        "Αλεξανδρίτης",
        "Αμέθυστος",
        "Αχάτης ",
        "Διαμάντι",
        "Ρουμπίνι ",
        "Ζαφείρι ",
        "Σμαράγδι",
        "Τιρκουάζ",
        "Στρας",
        "Ρόδι",
        "Μαργαριτάρι",
        "Νεφρίτης",
        "Τοπάζι",
        "Τουρμαλίνη",
        "Κιτρίνη",
        "Κεχριμπάρι",
    )

    def gemstone_name(self) -> str:
        """
        Return greek gemstone name randomly
        example: 'Κιτρίνη'
        """
        return self.random_element(self.gemstone_names)
