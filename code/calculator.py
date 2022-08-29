class Calculator:
    def add(self,x, y):
        result =  x + y
        return round(result, 2)

    def subtract(self,x, y):
        result = x - y
        return round(result, 2)

    def multiply(self,x, y):
        result = x * y
        return round(result, 2)

    def divide(self,x, y):
        if y == 0:
            result = 'Cannot divide by 0'
            return result
        result = x * 1.0 / y
        return round(result, 2)
