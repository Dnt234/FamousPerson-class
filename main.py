class FamousPerson:
    def __init__(self, name, birth_year=None, country_of_birth=None):
        self.name = name
        self.birth_year = birth_year  # Fixed: Assigning birth_year
        self.country_of_birth = country_of_birth  # Fixed: Assigning country_of_birth
    
    def introduce(self):
        print(f"Hi, my name is {self.name}. I was born in {self.birth_year} in {self.country_of_birth}.")

class Scientist(FamousPerson):
    def __init__(self, name, birth_year=None, country_of_birth=None, field=None, notable_discoveries=None):
        self.field = field
        self.notable_discoveries = notable_discoveries
        super().__init__(name, birth_year, country_of_birth)

    def introduce(self):
        super().introduce()
        print(f"I am a scientist known for my work in {self.field}. My notable discoveries include {self.notable_discoveries}.")

class Politician(FamousPerson):
    def __init__(self, name, birth_year=None, country_of_birth=None, years_in_office=None, political_position=None):
        self.years_in_office = years_in_office  # Fixed: Corrected attribute name
        self.political_position = political_position
        super().__init__(name, birth_year, country_of_birth)

    def introduce(self):
        super().introduce()
        print(f"I have served as {self.political_position} for {self.years_in_office} years.")



lebron_james = FamousPerson("LeBron James", 1984, "USA")
lebron_james.introduce()
print()
albert_einstein = Scientist("Albert Einstein", 1879, "Germany", "Theoretical Physics", "Theory of Relativity")
albert_einstein.introduce()
print()
abraham_lincoln = Politician("Abraham Lincoln", 1809, "USA", 4, "President")
abraham_lincoln.introduce()
print()


