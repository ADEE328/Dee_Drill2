
from pyscript import display

Basketball = {'Aaron', 'Euan', 'Harvey', 'Alijah','Marcus'}

Volleyball = {'Dee','Euan','Harvey','Alijah','Mergal'}

display(Basketball | Volleyball, target='output0') 
display(Basketball & Volleyball, target='output1') 
display(Basketball - Volleyball, target='output2')
display(Volleyball - Basketball, target='output3') 
display(Volleyball ^ Basketball, target='output4') 
