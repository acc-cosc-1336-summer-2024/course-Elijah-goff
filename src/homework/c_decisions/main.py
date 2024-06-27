from decisions import get_options_ratio
from decisions import get_faculty_rating

options = float(input('Score:')) 

total = float(input('Max Amount Of Score:')) 

ratio = (get_options_ratio(options, total))
ranking = (get_faculty_rating(ratio))

print('Your Faculty Rating As Follows: ', ranking)