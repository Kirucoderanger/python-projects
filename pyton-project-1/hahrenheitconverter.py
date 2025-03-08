#deg_far=input("insert the degree Fahrrenheit you want to convert: ")
deg_far=float(input("insert the degree Fahrrenheit you want to convert: "))

#deg_cel=(float(deg_far)-32)*(5/9) 
deg_cel=(deg_far-32)*(5/9) 

print(f"the converted degree celisous is {deg_cel:.1f} degrees.")