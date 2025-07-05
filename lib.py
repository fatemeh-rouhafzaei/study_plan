def grades_level (grades) :
        for key , Value in grades.items() :
            if 0 <= Value <= 50 :
                print("grades poor" , "=", key , ":" , Value)
            elif 50 < Value <= 75 :
                print("grades medium" , "=", key , ":" , Value)
            elif 75 < Value <= 100 :
                print("grades good" , "=", key , ":" , Value)
            else :
                 print("error")
def target(target , grade) :
    def konkur() :
        if  grade == "good" :
               for plan in grade :
                    return f'you can use plan_konkur_A for {plan} .'
        elif grade == "medium" :
               for plan in grade :
                    return f'you can use plan_konkur_B for {plan} .'                   
        elif grade == "poor" :
               for plan in grade :
                    return f'you can use plan_konkur_C for {plan} .'                   
    def final_exam() :
        if  grade == "good" :
            for plan in grade :
                return f'you can use plan_final exam_A for {plan} .'
        elif grade == "medium" :
            for plan in grade :
                return f'you can use plan_final exam_B for {plan} .'                   
        elif grade == "poor" :
            for plan in grade :
                return f'you can use plan_final exam_C for {plan} .'                   
    if target == "konkur" :
        return konkur 
    elif target == "final exam" :
        return final_exam
    else :
         return "error"
         