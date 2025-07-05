# grades = {

#     'riazi': 78,

#     'zist': 45,

#     'phizik': 62,

#     'shimi': 83
# # }

# def tt(grades):
#     print(list(grades.values()))

# o = tt({

#     'riazi': 78,

#     'zist': 45,

#     'phizik': 62,

#     'shimi': 83} )
# print(o)
# #def study_plan_generator(grades, target) :
# # def grades_level(grades) :

# #     for x, obj in grades.items():
# #         if grades <= 50 :
# #             print "poor"
# #         elif 50 < grades <= 75 :
# #             print "medium"
# #         elif 75 < grades <= 100 :
# #             print "good"
# #         else :
# #             print("error")
# o = [14,26,39,55,67]

# p =[x for x in o if x > 20] 
# print(p)
# grades =     'riazi': 78,

#     'zist': 45,

#     'phizik': 62,

#     'shimi': 83

# def o(grades) :
#     for w , e in grades.items() :
#         if e > 20 :
#             print(w  , ":" , e)
f = o({'riazi': 78,

    'zist': 45,

    'phizik': 62,

    'shimi': 83}) 
# print(f)           
# p = [o for o in grades if o > 20 ]

# print(p)
# def grades_level (grades) :
#     def grades_good () :
#         return 2
#     def grades_mdium(): 
#         return 1
#     def grades_poor () :
#         return 0
#     for key , Value in grades.items() :
#         if 0 <= Value <= 50 :
#             return grades_poor
#         elif 50 < Value <= 75 :
#             return grades_mdium
#         elif 75 < Value <= 100 :
#             return grades_good
#         else :
#             print("error")
# o = grades_level({'riazi': 78,'zist': 45,'phizik': 62,'shimi': 83})
# print(o)
# def target(target , grade, grades) :
#     def konkur() :
#         if  grade == "good" :
#                for plan in grade :
#                     return f'you can use plan_konkur_A for {plan} .'
#         elif grade == "medium" :
#                for plan in grade :
#                     return f'you can use plan_konkur_B for {plan} .'                   
#         elif grade == "poor" :
#                for plan in grade :
#                     return f'you can use plan_konkur_C for {plan} .'                   
#     def final_exam() :
#         if  grade == "good" :
#             for plan in grade :
#                 return f'you can use plan_final exam_A for {plan} .'
#         elif grade == "medium" :
#             for plan in grade :
#                 return f'you can use plan_final exam_B for {plan} .'                   
#         elif grade == "poor" :
#             for plan in grade :
#                 return f'you can use plan_final exam_C for {plan} .'                   
#     if target == "konkur" :
#         return konkur 
#     elif target == "final exam" :
#         return final_exam
#     else :
#          return "error"
# o = target("konkur" , "good")()
# print(o)
g = grades_level({'riazi': 78,

    'zist': 45,

    'phizik': 62,

    'shimi': 83})

def grades_level (grades) :
    grades={'riazi': 78,

    'zist': 45,

    'phizik': 62,

    'shimi': 83}
    grade = [level for level in grades.values() if 0 <= level <= 50 ]
    