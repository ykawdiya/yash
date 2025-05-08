# Expert System on Employee Performance Evaluation
class Evaluation:
    def __init__(self) -> None:
        print("\n" + "=" * 50)
        print(" EMPLOYEE PERFORMANCE EVALUATION SYSTEM ")
        print("=" * 50)
        self.name = input("\nEnter name of employee: ")
        
        # Initialize competencies with [rating, weightage, weighted_score]
        self.competencies = {
            "Communication": [0, 0, 0],
            "Productivity": [0, 0, 0],
            "Creativity": [0, 0, 0],
            "Integrity": [0, 0, 0],
            "Punctuality": [0, 0, 0]
        }
        
        # Initialize performance goals with [rating, weightage, weighted_score]
        self.performance = {
            "Goal 1": [0, 0, 0],
            "Goal 2": [0, 0, 0],
            "Goal 3": [0, 0, 0],
            "Goal 4": [0, 0, 0],
            "Goal 5": [0, 0, 0]
        }

    def printTable(self, hashMap: dict):
        if hashMap == self.competencies:
            print("\n-=-= Competency Goals =-=-")
            print(f"{'Competency':<15} {'Rating':^8} {'Weightage':^10} {'Weighted Score':^15}")
            print("-" * 50)
            for key, value in self.competencies.items():
                print(f"{key:<15} {value[0]:^8} {value[1]:^10} {value[2]:^15.2f}")
            print()
        else:
            print("\n-=-= Performance Goals =-=-")
            print(f"{'Goals':<15} {'Rating':^8} {'Weightage':^10} {'Weighted Score':^15}")
            print("-" * 50)
            for key, value in self.performance.items():
                print(f"{key:<15} {value[0]:^8} {value[1]:^10} {value[2]:^15.2f}")
            print()

    def input_data(self):
        print("\n" + "-" * 50)
        print(" RATING AND WEIGHTAGE INPUT ")
        print("-" * 50)
        print("\nPlease rate on scale: 1=Below Expectations, 2=Meets Expectations, 3=Exceeds Expectations")
        print("NOTE: Weightage must total 100 for each section")
        
        # Competencies input
        print("\n" + "-" * 25)
        print(" COMPETENCY EVALUATION ")
        print("-" * 25)
        weightTotal = 0
        for key in self.competencies.keys():
            while True:
                try:
                    print(f"\n>> {key}:")
                    rating = int(input(f"   Rating (1-3): "))
                    if rating < 1 or rating > 3:
                        print("   ERROR: Rating must be between 1-3.")
                        continue
                    
                    weightage = int(input(f"   Weightage (remaining: {100 - weightTotal}): "))
                    if weightage < 0 or weightage > 100 - weightTotal:
                        print(f"   ERROR: Weightage must be between 0-{100 - weightTotal}.")
                        continue
                    
                    self.competencies[key][0] = rating
                    self.competencies[key][1] = weightage
                    weightTotal += weightage
                    break
                except ValueError:
                    print("   ERROR: Please enter valid numbers.")
        
        # Performance goals input
        print("\n" + "-" * 25)
        print(" PERFORMANCE EVALUATION ")
        print("-" * 25)
        weightPerformanceTotal = 0
        for key in self.performance.keys():
            while True:
                try:
                    print(f"\n>> {key}:")
                    rating = int(input(f"   Rating (1-3): "))
                    if rating < 1 or rating > 3:
                        print("   ERROR: Rating must be between 1-3.")
                        continue
                    
                    weightage = int(input(f"   Weightage (remaining: {100 - weightPerformanceTotal}): "))
                    if weightage < 0 or weightage > 100 - weightPerformanceTotal:
                        print(f"   ERROR: Weightage must be between 0-{100 - weightPerformanceTotal}.")
                        continue
                    
                    self.performance[key][0] = rating
                    self.performance[key][1] = weightage
                    weightPerformanceTotal += weightage
                    break
                except ValueError:
                    print("   ERROR: Please enter valid numbers.")

    def calcScore(self):
        for key in self.competencies.keys():
            self.competencies[key][2] = self.competencies[key][0] * self.competencies[key][1] / 100
        for key in self.performance.keys():
            self.performance[key][2] = self.performance[key][0] * self.performance[key][1] / 100

    def calculate(self):
        # Collect input from user
        self.input_data()
        
        # Calculate weighted scores
        self.calcScore()
        
        # Display results
        print("\n" + "=" * 50)
        print(" EVALUATION RESULTS ")
        print("=" * 50)
        
        # Show competencies table
        self.printTable(self.competencies)

        sumCompetency = 0
        for key in self.competencies.keys():
            sumCompetency += self.competencies[key][2]
        print(f"\nSum of weighted scores - Competency: {sumCompetency:.2f}")
        
        self.printTable(self.performance)
        sumPerformance = 0
        for key in self.performance.keys():
            sumPerformance += self.performance[key][2]
        print(f"\nSum of weighted scores - Performance: {sumPerformance:.2f}")
        
        # Calculate the average of both sections (not the sum)
        total = (sumCompetency + sumPerformance) / 2
        
        print("\n" + "=" * 50)
        print(f"Employee Evaluation Summary for: {self.name}")
        print("=" * 50)
        print(f"Competency Score: {sumCompetency:.2f}")
        print(f"Performance Score: {sumPerformance:.2f}")
        print(f"Overall Rating (out of 3): {total:.2f}")
        
        if total >= 2.7:
            print("\nVerdict: Employee EXCEEDS expectations")
        elif total >= 1.7:
            print("\nVerdict: Employee MEETS expectations")
        else:
            print("\nVerdict: Employee FAILS expectations")
        print("=" * 50)


obj = Evaluation()
obj.calculate()