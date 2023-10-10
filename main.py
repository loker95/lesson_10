class City:
    def __init__(self, city_name, county_name, country_name, amount_of_citizens, post_code, phone_code_number):
        self.__city_name = city_name
        self.__county_name = county_name
        self.__country_name = country_name
        self.__amount_of_citizens = amount_of_citizens
        self.__post_code = post_code
        self.__phone_code_number = phone_code_number

    def set_coord(self, city_name, county_name, country_name, amount_of_citizens, post_code, phone_code_number):
        self.__city_name = city_name
        self.__county_name = county_name
        self.__country_name = country_name
        self.__amount_of_citizens = amount_of_citizens
        self.__post_code = post_code
        self.__phone_code_number = phone_code_number

    def get_coord(self):
        return (self.__city_name, self.__county_name, self.__country_name,
                self.__amount_of_citizens, self.__post_code, self.__phone_code_number)

    def show_details(self):
        print(f"city name - {self.__city_name}, conty name - {self.__county_name},"
              f" country name - {self.__country_name}, amount of citizens -"
              f" {self.__amount_of_citizens}, post code - {self.__post_code},"
              f" phone code number - {self.__phone_code_number}")

    @staticmethod
    def show_info():
        print(London)
        print("this city")


London = City("London", "UK", "Greater London",
              16000000, "SW1", "+44")
London.show_details()
London.show_info()


class Country:
    def __init__(self, country_name, continent_name, citizens_amount, phone_code, capital_name, cities_names):
        self.__country_name = country_name
        self.__continent_name = continent_name
        self.__citizens_amount = citizens_amount
        self.__phone_code = phone_code
        self.__capital_name = capital_name
        self.__cities_names = cities_names

    def set_coord(self, country_name, continent_name, citizens_amount, phone_code, capital_name, cities_names):
        self.__country_name = country_name
        self.__continent_name = continent_name
        self.__citizens_amount = citizens_amount
        self.__phone_code = phone_code
        self.__capital_name = capital_name
        self.__cities_names = cities_names

    def get_coord(self):
        return (self.__country_name, self.__continent_name, self.__citizens_amount,
                self.__phone_code, self.__capital_name, self.__cities_names)

    def show_info(self):
        print(f"Название страны - {self.__country_name}, имя континента - {self.__continent_name},"
              f" количество жителей - {self.__citizens_amount}, телефонный код - {self.__phone_code},"
              f" столица - {self.__capital_name}, города - {self.__cities_names}")


UK = Country("united kingdom", "Eurasia", 46000000,
             "+44", "London", "London, Manchester, Liverpool")

Country.show_info(UK)