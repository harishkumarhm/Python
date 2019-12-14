import random

class Coin:
    def __init__(self,rare=False, clean = True, heads= True, **kwargs):

        for key, value in kwargs.items():
            setattr(self,key,value)
            
        self.is_rare = rare
        self.is_clean = clean
        self.is_heads = heads

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.color = self.original_color
        else:
            self.color = self.rust_color
            
    def __del__(self):
        print("Coin spent!")
        
    def rust(self):
        self.color = "greenish"
    def clean(self):
        self.color = "gold"
    
    def flip(self ):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
        
    def __str__(self):
        if self.original_value > 1:
           return "{}$ coin".format(int(self.value))
        else:
            return "{} Pence".format(int(self.value*10))

    
class One_Pence(Coin):
    
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "gold",
            "original_value" : 0.1,
            "diameter" : 25.5, #mm
            "thickness" : 1.5, #mm
            "mass": 10.5
            }
        super().__init__(**data)
    

class Two_Pence(Coin):
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "gold",
            "original_value" : 0.2,
            "diameter" : 25.5, #mm
            "thickness" : 1.5, #mm
            "mass": 9.5
            }
        super().__init__(**data)

class Five_Pence(Coin):
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "gold",
            "original_value" : 0.5,
            "diameter" : 25.5, #mm
            "thickness" : 1.5, #mm
            "mass": 9.5
            }
        super().__init__(**data)
            
class Twenty_Pound(Coin):
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "greenish",
            "original_value" : 20,
            "diameter" : 25.5, #mm
            "thickness" : 1.5, #mm
            "mass": 9.5
            }
        super().__init__(**data)
    

class Five_Pound(Coin):
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "greenish",
            "original_value" : 0.5,
            "diameter" : 25.5, #mm
            "thickness" : 1.5, #mm
            "mass": 9.5
            }
        super().__init__(**data)
           
class Pound(Coin):
    
    def __init__(self):
        data = {
            "original_color" : "gold",
            "rust_color" : "greenish",
            "original_value" : 1,
            "diameter" : 22.5, #mm
            "thickness" : 1.0, #mm
            "mass": 9.5
            }
        super().__init__(**data)
      
    
        
coins =[Pound(), Five_Pound(), Twenty_Pound(), One_Pence(), Two_Pence(), Five_Pence()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.original_color,coin.rust_color,coin.mass]
    strng = "{}: color-{}, value-{}, original_color-{}, rust_color-{}, mass -{}".format(*arguments)
    print(strng)
