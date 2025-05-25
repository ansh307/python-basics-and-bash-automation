def vac_feedback(vac, effeciency):
    print(f"Vaccine: {vac}")
    print(f"Effeciency: {effeciency}")
    
    if effeciency > 50 and effeciency < 75:
        print("This vaccine is moderately effective.")
    elif effeciency >= 75 and effeciency <= 90:
        print("This vaccine is highly effective.")
    else:
        print("This vaccine is not effective.")
        

vac_feedback("Pfizer", 95)
print("")
vac_feedback("Moderna", 70)
print("")
vac_feedback("AstraZeneca", 60)
print("")
vac_feedback(effeciency=40, vac="Sinovac")
