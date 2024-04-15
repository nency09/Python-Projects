import requests
import matplotlib.pyplot as plt
from datetime import datetime

class Weather:
    #CONSTRUCTOR FOR INTIALISING ALL LISTS

    def __init__(self):
        self.city_name = None
        self.temp_list = []
        self.feels_like_list = []
        self.temp_max_list = []
        self.temp_min_list = []
        self.weh_list = []
        self.pre_list = []
        self.win_list = []
        self.vis_list = []
        self.hum_list = []
        self.cloudiness_list = []
        self.sunrise_list = []
        self.sunset_list = []
        self.date_list = []
        self.dis_list=[]

  #SETS CITY NAME
    def set_city_name(self, city_name):
        self.city_name = city_name

 #FETCHES DATA AND APPENDING TO THE LIST
    def weather_data(self):
        api_key = "28afca387834754b8492138f67ed23fe"
        api_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
        query_params = {'q': self.city_name, 'appid': api_key, 'units': 'metric'}

        response = requests.get(api_endpoint, params=query_params)

        if response.status_code == 200:
            data = response.json()
            for i in range(0 ,len(data['list']), 8):
                temp = data['list'][i]['main']['temp']
                feels_like = data['list'][i]['main']['feels_like']
                temp_max = data['list'][i]['main']['temp_max']
                temp_min = data['list'][i]['main']['temp_min']
                weather = data['list'][i]['weather'][0]['main']
                pressure = data['list'][i]['main']['pressure']
                wind_speed = data['list'][i]['wind']['speed']
                visibility = data['list'][i]['visibility']
                humidity = data['list'][i]['main']['humidity']
                cloudiness = data['list'][i]['clouds']['all']
                sunrise = datetime.fromtimestamp(data['city']['sunrise'])
                sunset = datetime.fromtimestamp(data['city']['sunset'])
                date_time = datetime.fromtimestamp(data['list'][i]['dt'])
                dis=data['list'][i]["weather"][0]["description"]
                
                #appending data in the list
                self.temp_list.append(temp)
                self.feels_like_list.append(feels_like)
                self.temp_max_list.append(temp_max)
                self.temp_min_list.append(temp_min)
                self.weh_list.append(weather)
                self.pre_list.append(pressure)
                self.win_list.append(wind_speed)
                self.vis_list.append(visibility)
                self.hum_list.append(humidity)
                self.cloudiness_list.append(cloudiness)
                self.sunrise_list.append(sunrise)
                self.sunset_list.append(sunset)
                self.date_list.append(date_time)
                self.dis_list.append(dis)
        else:
            print(f'Error: {response.status_code} - {response.text}')
            
            
    def current_data(self):
                print("Date:", self.date_list[0].strftime("%Y-%m-%d %H:%M:%S"))
                print('Temperature:', self.temp_list[0], '°C')
                print('Feels Like:', self.feels_like_list[0], '°C')
                print('Max Temperature:', self.temp_max_list[0], '°C')
                print('Min Temperature:', self.temp_min_list[0], '°C')
                print('Weather:', self.weh_list[0])
                print('Pressure:', self.pre_list[0], 'hPa')
                print('Wind Speed:', self.win_list[0], 'm/s')
                print('Visibility:', self.vis_list[0], 'm')
                print('Humidity:', self.hum_list[0], '%')
                print('Cloudiness:', self.cloudiness_list[0], '%')
                print('Sunrise Time:', self.sunrise_list[0].strftime("%Y-%m-%d %H:%M:%S"))
                print('Sunset Time:', self.sunset_list[0].strftime("%Y-%m-%d %H:%M:%S"))
                print()
                print("-------------------------DISCRIPTION------------------------")
                print("current conditions are going to be ",self.dis_list[0])
                print(self.dis_list)
    
        #FETCHING 5 DAYS DATA THROUGH API
    def view_5days_data(self):
        for i in range(5):
            print("Date:", self.date_list[i].strftime("%Y-%m-%d %H:%M:%S"))
            print('Temperature:', self.temp_list[i], '°C')
            print('Feels Like:', self.feels_like_list[i], '°C')
            print('Max Temperature:', self.temp_max_list[i], '°C')
            print('Min Temperature:', self.temp_min_list[i], '°C')
            print('Weather:', self.weh_list[i])
            print('Pressure:', self.pre_list[i], 'hPa')
            print('Wind Speed:', self.win_list[i], 'm/s')
            print('Visibility:', self.vis_list[i], 'm')
            print('Humidity:', self.hum_list[i], '%')
            print('Cloudiness:', self.cloudiness_list[i], '%')
            print('Sunrise Time:', self.sunrise_list[i].strftime("%Y-%m-%d %H:%M:%S"))
            print('Sunset Time:', self.sunset_list[i].strftime("%Y-%m-%d %H:%M:%S"))
            print()
            print("-------------------------DISCRIPTION------------------------")
            print(f"Day {i+1} conditions are going to be ",self.dis_list[i])

  #CLEAR ALL DATA FROM THE LIST
    def get_new_forecast(self):
        self.temp_list.clear()
        self.feels_like_list.clear()
        self.temp_max_list.clear()
        self.temp_min_list.clear()
        self.weh_list.clear()
        self.pre_list.clear()
        self.win_list.clear()
        self.vis_list.clear()
        self.hum_list.clear()
        self.cloudiness_list.clear()
        self.sunrise_list.clear()
        self.sunset_list.clear()
        self.date_list.clear()
        #self.weather_data()
        #self.view_5days_data()


 #for plotting graphs
    def plot_parameter(self, parameter):
        if parameter == 1:
            plt.plot(self.date_list, self.temp_list, marker='o', linestyle='-')
            plt.xlabel('Date')
            plt.ylabel('Temperature (°C)')
            plt.title('Temperature Variation')
            plt.xticks(rotation=45)
            plt.show()
        elif parameter == 2:
            plt.plot(self.date_list, self.pre_list, marker='o', linestyle='-')
            plt.xlabel('Date')
            plt.ylabel('Pressure (hPa)')
            plt.title('Pressure Variation')
            plt.xticks(rotation=45)
            plt.show()
        elif parameter == 3:
            plt.plot(self.date_list, self.hum_list, marker='o', linestyle='-')
            plt.xlabel('Date')
            plt.ylabel('Humidity (%)')
            plt.title('Humidity Variation')
            plt.xticks(rotation=45)
            plt.show()
        elif parameter == 4:
            plt.plot(self.date_list, self.cloudiness_list, marker='o', linestyle='-')
            plt.xlabel('Date')
            plt.ylabel('Cloudiness (%)')
            plt.title('Cloudiness Variation')
            plt.xticks(rotation=45)
            plt.show()
        else:
            print('Invalid parameter. Please choose from temperature, pressure, humidity, cloudiness, wind_direction, or uv_index.')

    def change_location(self):
        new_city = input("Enter new city name: ")
        self.get_new_forecast()
        #print('clear list',self.cloudiness_list)
        self.set_city_name(new_city)
        self.weather_data()


weather_obj = Weather()

city_name = input("Enter city name: ")
weather_obj.set_city_name(city_name)

weather_obj.weather_data()

while True:
    print()
    print("---------------OPTIONS---------------")
    print("1. View current data")
    print("2. Get forecast for the next 5 days")
    print("3. Plot specific weather parameter")
    print("4. Change location")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        weather_obj.current_data()
    elif choice == '2':
        weather_obj.view_5days_data()
    elif choice == '3':
        parameter = int(input("Enter weather parameter to plot (1.temperature,2.pressure,3.humidity,4.cloudiness): "))
        weather_obj.plot_parameter(parameter)
    elif choice == '4':
        weather_obj.change_location()
    elif choice == '5':
        print("----------THANK YOU----------")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
