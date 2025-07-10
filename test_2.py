def study_plan(grades , target) :
    def grades_level(score):
        if 0 <= Score <= 50 :
            return "poor" 
        elif 50 < Score <= 75 :
            return "medium"
        elif 75 < Score <= 100 :
            return "good"
        else :
            print("error_grades_value")


    def suggst_plan (level) :
        def final_exam () :
            pass
        def konkur() :
            pass
        if target == "konkur" :
            return konkur()
        else :
            return final_exam() 
    plan={}
    for subject , score in grades.items() :
        level = grades_level(score) 
        strategy = suggst_plan(level) 
        plan[subject] = f"{level}:{strategy}"
    return plan 
    