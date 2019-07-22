class Farm:
    all_farms = []
    food_per_hectare={
        'corn': 20,
        'wheat': 30
    }
    total_crop = 0

    def __init__(self,size,crop):
        self.size = size
        self.crop = crop
        
    @classmethod
    def add_farm(cls,size,crop):
        new_farm = Farm(size,crop)
        cls.all_farms.append(new_farm)
        return new_farm
    @classmethod
    def harvest_crops(cls):
        for farm in cls.all_farms:
            current_farm_harvest = cls.food_per_hectare[farm.crop]*farm.size
            print(f'Harvesting {current_farm_harvest}, from {farm.size} hectare {farm.crop} field')
            cls.total_crop += current_farm_harvest
        return cls.total_crop
    @classmethod
    def farm_status(cls):
        for farm in cls.all_farms:
            print(f'{farm.crop.capitalize()} field is {farm.size} hectares')
        print(f'Harvested {cls.total_crop} food so far')