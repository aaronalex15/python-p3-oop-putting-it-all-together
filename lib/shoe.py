#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            raise ValueError('size must be an integer')
        self.size = size
        self.condition = "New"  
    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = "New"



