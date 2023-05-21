import matplotlib.pyplot as plt

class Grade:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    
    def avg(self):
        return (self.kor + self.eng + self.math) / 3.0
    

class VisualEx:
    def basic_example(self):
        path = 'static/plot_ex.png'
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.savefig(path)
        return path
    
        
