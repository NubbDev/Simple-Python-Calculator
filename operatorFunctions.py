from tkinter import Button

class operators:
    def __init__(self, frame, equation, expression):
        self.equation = equation
        self.expression = expression
        self.frame = frame
    
    def clear(self):
        self.equation.clear()
        self.expression.set(''.join(self.equation))
        print(self.equation)
    def delete(self):
        if len(self.equation) > 0:
            self.equation.pop()
            self.expression.set(''.join(self.equation))
            print(self.equation)
        else: 
            print("No equation")
    def input(self, value): 
        self.equation.append(value)
        print(''.join(self.equation))
        # self.expression.set(''.join(self.equation))
    def solve(self):
        if (len(self.equation) > 0):
            self.expression.set(eval(''.join(self.equation)))
            self.equation.clear()
        else: 
            try: 
                sol = eval(''.join(self.expression.get()))
                self.expression.set(sol) 
                self.equation.clear()
            except Exception as e:
                self.equation.clear()
                self.expression.set("Error")
                print(e)
    def buttons(self, text, value):
        return Button(self.frame, text=text, command=lambda: self.input(value))
    def updateHandler(self):
        temp = [*self.expression.get()]
        self.equation.clear()
        self.equation.append(temp)
        print(temp)
    ##End of the File2