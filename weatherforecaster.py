import requests 

print("\t Welcome to the Weather Forecaster!\n\n")
print("Just enter the city you want the weather report for and click on the button!\n\n")

cityName = input("Enter the name of the city: ")
print("\n\n")

def genReport(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error occured"
    print(T)

genReport(cityName)