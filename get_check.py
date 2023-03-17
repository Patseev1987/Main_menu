def get_check(string,all_data):
  count=0
  if string.replace(" ","")=="":
    print("You didn't enter any information")
    return False
  for i in all_data:
    new_string=i.split()
    arrrr=""
    for x in range(1,len(new_string)):
     arrrr+=new_string[x].strip()+" "
    if string.lower().strip()==arrrr.lower().strip():
     count+=1
  if count>0:
    print("You have this contact")
    return False
  return True