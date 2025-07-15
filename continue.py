cart=[10,20,30,600,700,80,90]
for item in cart:
    if item>500:
        print("To place this order insurance must be required",item)
        continue
    print('processing ...item')
