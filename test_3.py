class evaluate_level :
    def evaluate_level(self , score):
        if score < 50:
            return 'poor'
        elif score < 75:
            return 'average'
        else:
            return 'good'
class StudyAdvisor(evaluate_level):
    def __init__(self , target):
        self.target = target
    def __call__(self, grades:dict):
        plan = {}
        for subject , score in grades.items():
            level = evaluate_level.evaluate_level(score)
            strategy = suggest_strategy.suggest_strategy(level)
            plan[subject] = f'{level}: {strategy}'
        return plan
class suggest_strategy:
    def suggest_strategy(self , level):
        if self.target == 'konkur':
           strategies = {
               'poor' : 'Thorough textbook review + Fundamental practice questions',
               'average' : 'Focus on frequently asked questions',
               'good' : 'Review of challenging questions'
           } 
        else:
            strategies = {
                'poor' : 'Comprehensive review + Practice with basic questions',
                'average' : 'Practice questions + Review of key points',
                'good' : 'Quick review of important concepts'
            }
        return strategies.get(level, "No strategy found")

target = 'final_exam'
grades = {
    'riazi': 78,
    'zist': 45,
    'phizik': 62,
    'shimi': 83
}


advisor = StudyAdvisor(target)
reslut = advisor(grades)
print("target:",target)
for subject , message in reslut.items():
    print(f"{subject}: {message}")
# class evaluate_level:
#     def evaluate_level(self, score):
#         if score < 50:
#             return 'poor'
#         elif score < 75:
#             return 'average'
#         else:
#             return 'good'

# class suggest_strategy:
#     def init(self, target):
#         self.target = target

#     def suggest_strategy(self, level):
#         if self.target == 'konkur':
#             strategies = {
#                 'poor': 'Thorough textbook review + Fundamental practice questions',
#                 'average': 'Focus on frequently asked questions',
#                 'good': 'Review of challenging questions'
#             }
#         else:
#             strategies = {
#                 'poor': 'Comprehensive review + Practice with basic questions',
#                 'average': 'Practice questions + Review of key points',
#                 'good': 'Quick review of important concepts'
#             }
#         return strategies.get(level, "No strategy found")

# class StudyAdvisor(evaluate_level):
#     def init(self, target):
#         # self.target = target
#         self.strategy_advisor = suggest_strategy(target)

#     def call(self, grades: dict):
#         plan = {}
#         for subject, score in grades.items():
#             level = self.evaluate_level(score)
#             strategy = self.strategy_advisor.suggest_strategy(level)
#             plan[subject] = f'{level}: {strategy}'
#         return plan

# # استفاده:
# target = 'final_exam'
# grades = {
#     'riazi': 78,
#     'zist': 45,
#     'phizik': 62,
#     'shimi': 83
# }

# advisor = StudyAdvisor(target)
# result = advisor(grades)

# print("target:", target)
# for subject, message in result.items():
#     print(f"{subject}: {message}")