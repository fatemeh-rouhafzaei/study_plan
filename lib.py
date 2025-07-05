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


