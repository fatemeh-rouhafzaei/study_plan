grades_poor = []
grades_medium = []
grades_good = []
# this def get a plan for study 
def study_plan_generator(grades , target):
    for key, Value in grades.items() :
        if 0 <= Value <= 50 :
            return grades_poor_list 
        elif 50 < Value <= 75 :
            return grades_medium_list 
        elif 75 < Value <= 100 :
            return grades_good_list
        else :
            print("error_grades_value")

#the following def categorizes grades into three gruops.
    def grades_poor_list() :
        grades_poor.append(key)
        return grades_poor
    def grades_medium_list() :
        grades_medium.append(key)
        return grades_medium
    def grades_good_list() :
        grades_good.append(key)
        return grades_good
    
#this def provides you with a program based on the specified goal.
    def target_study_plan() :
        if target == 0 :
            return konkur_target 
        elif target == 1 :
            return final_target
        else :
            print("error target")        
        def konkur_target() :
            def konkur_poor_grades() :
                for lesson in grades_poor :
                    return f'you can use plan_konkur_C for lesson{lesson}'
            def konkur_medium_grades() :
                for lesson in grades_medium :
                        return f'you can use plan_konkur_B for lesson{lesson}'       
            def konkur_good_grades() :
                for lesson in grades_good :
                    return f'you can use plan_konkur_A for lesson{lesson}' 

        def final_target() :
            def final_poor_grades() :
                for lesson in grades_poor :
                    return f'you can use plan_final_C for lesson{lesson}'
            def final_medium_grades() :
                for lesson in grades_medium :
                    return f'you can use plan_final_B for lesson{lesson}'       
            def final_good_grades() :
                for lesson in grades_good :
                    return f'you can use plan_final_A for lesson{lesson}' 

         
         