from .. import Provider as GeographyProvider


class Provider(GeographyProvider):
    mountain_names = (
        "Αιγάλεω",
        "Άθως",
        "Αίνος",
        "Αίτνα",
        "Άλπεις",
        "Αππένινα",
        "Αροανία",
        "Βεργίνα",
        "Γερανεία",
        "Δίβρη",
        "Δίρφυς",
        "Έλικον",
        "Ζήρια",
        "Κυλλήνη",
        "Λυκαβηττός",
        "Μαίναλον",
        "Μίνθη",
        "Οινόη",
        "Οίτη",
        "Όλυμπος",
        "Όλυμπος",
        "Κίσσαβος",
        "Παντωκράτορ",
        "Παρνασσός",
        "Πάρνηθα",
        "Πεννίοες",
        "Πεντέλη",
        "Πήλιον",
        "Πίνδος",
        "Σκόλλις",
        "Ταΰγετος",
        "Υμηττός",
        "Φολόη",
        "Χελμός",
    )

    def mountain_name(self) -> str:
        """
        Return greek mountain name randomly
        example: 'Υμηττός'
        """
        return self.random_element(self.mountain_names)
