from farm import Farm

class Farmer:
    def main_menu(self):
        while True:
            self.print_main_menu()
            user_input = input()
            self.call_option(user_input)
    
    def print_main_menu(self):
        print("---------------------------")
        print("Field -> adds a new field")
        print("Harvest -> harvests crops and adds to total harvested")
        print("Status -> displays some information about the farm")
        print("Relax -> provides lovely descriptions of your fields")
        print("Exit -> exits the program")
        print("---------------------------")
    def call_option(self,user_input):
        if user_input.lower() == "field":
            self.new_farm()
        elif user_input.lower() == 'harvest':
            self.harvest()
        elif user_input.lower() == 'status':
            self.status()
        elif user_input.lower() == 'relax':
            self.relax()
        elif user_input.lower() == 'exit':
            exit("Goodbye")
        else:
            print("Error, invalid input")
    
    def new_farm(self):
        print("what kind of farm is it: corn or wheat?")
        field_type = input().lower()
        print("How large is the field in hectares?")
        field_size = int(input())
        Farm.add_farm(field_size, field_type)
        print(f'Added a {field_type.capitalize()} field of {field_size} Hectares')
    
    def harvest(self):
        total = Farm.harvest_crops()
        print(f'The farm has harvested {total} food so far')
    
    def status(self):
        Farm.farm_status()
    
    def relax(self):
        for farm in Farm.all_farms:
            if farm.crop == 'wheat':
                print(f'The sun hangs low, casting an orange glow on a sea of {farm.size} hectares of wheat.')
            elif farm.crop == 'corn':
                print(f'{farm.size} hectares of tall green stalks rustling in the breeze fill your horizon.')

adam = Farmer()
adam.main_menu()