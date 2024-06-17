ratio = 0 

def get_options_ratio(options, total):
  ratio = options / total #will do decimal operation
  return ratio

def get_faculty_rating(ratio):
    result = ""

    if(ratio >= .9 and ratio < 1):
      result = "Excellent"
    elif (ratio < .9 and ratio >= .8):
     result = "Very Good"
    elif (ratio < .8 and ratio >= .7 ):
     result = "Good"
    elif (ratio < .7 and ratio >= .6 ):
     result = "Needs Improvement"
    elif (ratio < .6 and ratio >= 0):
     result = "Unacceptable" 
    else:
     result = "Invalid Data" 

    return result    
