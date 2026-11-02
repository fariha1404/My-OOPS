class fruit:
    
    # Constructor
    def __init__(self, name, color):
        self.name = name 
        self.color = color
        
# Object Creation
strawberry = fruit('Strawberry', 'Red')
# Calling Function
print(strawberry.name)
print(strawberry.color)