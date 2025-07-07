def study_plan(grades , target) :
    def grades_level(score):
        pass
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
    