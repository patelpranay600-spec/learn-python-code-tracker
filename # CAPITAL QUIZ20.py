# CAPITAL QUIZ
import random
lai= input("if you want to continue press Y or N")
lst1=[]


capital_cities= {
    "Paris": "France", "Berlin": "Germany", "Rome": "Italy",
    "Madrid": "Spain", "Lisbon": "Portugal", "Athens": "Greece",
    "Tokyo": "Japan",  "Beijing": "China", "New Delhi": "India",
    "Brasília": "Brazil", "Canberra": "Australia", "Ottawa": "Canada",
    "Washington, D.C.": "United States",  "Moscow": "Russia", "London": "United Kingdom",
    "Cairo": "Egypt", "Pretoria": "South Africa", "Nairobi": "Kenya",
    "Buenos Aires": "Argentina", "Lima": "Peru", "Oslo": "Norway",
    "Stockholm": "Sweden", "Helsinki": "Finland", "Copenhagen": "Denmark",
    "Wellington": "New Zealand", "Vienna": "Austria", "Brussels": "Belgium",
    "Amsterdam": "Netherlands", "Dublin": "Ireland", "Seoul": "South Korea",
    "Bangkok": "Thailand", "Kuala Lumpur": "Malaysia", "Jakarta": "Indonesia",
    "Singapore": "Singapore", "Ankara": "Turkey", "Riyadh": "Saudi Arabia",
    "Abu Dhabi": "United Arab Emirates", "Tehran": "Iran", "Baghdad": "Iraq",
    "Jerusalem": "Israel", "Mexico City": "Mexico", "Santiago": "Chile",
    "Bogotá": "Colombia", "Quito": "Ecuador", "Caracas": "Venezuela",
    "Sucre": "Bolivia", "Asunción": "Paraguay", "Montevideo": "Uruguay",
    "Georgetown": "Guyana", "Havana": "Cuba", "Santo Domingo": "Dominican Republic",
    "San Salvador": "El Salvador", "Guatemala City": "Guatemala", "Tegucigalpa": "Honduras",
    "Managua": "Nicaragua", "San José": "Costa Rica", "Panama City": "Panama",
    "Kingston": "Jamaica", "Nassau": "Bahamas", "Port-au-Prince": "Haiti",
    "Philipsburg": "Sint Maarten", "Reykjavik": "Iceland", "Warsaw": "Poland",
    "Budapest": "Hungary", "Bucharest": "Romania", "Sofia": "Bulgaria",
    "Zagreb": "Croatia", "Ljubljana": "Slovenia", "Bratislava": "Slovakia",
    "Prague": "Czech Republic", "Belgrade": "Serbia", "Sarajevo": "Bosnia and Herzegovina",
    "Podgorica": "Montenegro", "Pristina": "Kosovo", "Skopje": "North Macedonia",
    "Tirana": "Albania", "Valletta": "Malta", "Nicosia": "Cyprus",
    "Yerevan": "Armenia", "Baku": "Azerbaijan", "Tbilisi": "Georgia",
    "Kiev": "Ukraine", "Minsk": "Belarus", "Vilnius": "Lithuania",
    "Riga": "Latvia", "Tallinn": "Estonia", "Hanoi": "Vietnam",
    "Phnom Penh": "Cambodia", "Vientiane": "Laos", "Rangoon": "Myanmar",
    "Manila": "Philippines", "Kathmandu": "Nepal", "Colombo": "Sri Lanka",
    "Dhaka": "Bangladesh", "Thimphu": "Bhutan", "Male": "Maldives",
    "Islamabad": "Pakistan", "Kabul": "Afghanistan", "Tashkent": "Uzbekistan",
    "Dushanbe": "Tajikistan", "Ashgabat": "Turkmenistan", "Bishkek": "Kyrgyzstan",
    "Nur-Sultan": "Kazakhstan", "Ulaanbaatar": "Mongolia", "Pyongyang": "North Korea",
    "Bandar Seri Begawan": "Brunei", "Taipei": "Taiwan", "Hong Kong": "Hong Kong",
    "Macau": "Macau", "Canberra": "Australia", "Rabat":"Morocco"
}


non_capital_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
   "Miami", "Toronto", "Vancouver", "Montreal", "Calgary",
   "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
   "Manchester", "Birmingham", "Liverpool", "Glasgow",
   "Marseille", "Lyon", "Toulouse", "Nice", "Nantes",
   "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart",
   "Milan", "Naples", "Turin", "Palermo", "Genoa",
   "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga",
   "Porto", "Funchal", "Braga", "Setúbal",
   "Thessaloniki", "Patras", "Larissa", "Heraklion", "Volos",
   "Yokohama", "Osaka", "Nagoya", "Sapporo", "Kobe",
   "Shanghai", "Guangzhou", "Shenzhen", "Chongqing", "Chengdu",
   "Mumbai", "Bangalore", "Hyderabad", "Ahmedabad", 
   "Rio de Janeiro", "São Paulo", "Salvador", "Fortaleza", "Belo Horizonte", 
   "Medellin", "Cali", "Barranquilla", "Cartagena",
   "Lima", "Arequipa", "Trujillo", "Chiclayo", "Iquitos",
   "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata",
   "Auckland", "Christchurch", "Hamilton", "Tauranga",
   "Dubai", "Sharjah", "Al Ain", "Ajman", "Istanbul",
   "Izmir", "Bursa", "Antalya", "Jeddah", "Mecca", 
   "Medina", "Dammam", "Durban", "Johannesburg",
   "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Lagos", 
   "Kano", "Ibadan", "Kaduna", "Port Harcourt", "Casablanca",
   "Fes", "Marrakech", "Tangier", "Accra", "Kumasi",
   "Tamale", "Sekondi-Takoradi", "Cape Coast", "Ho Chi Minh City", "Da Nang",
   "Hai Phong", "Can Tho", "Chiang Mai", "Pattaya", "Phuket",
   "Khon Kaen", "Penang", "Johor Bahru", "Ipoh", "Kuching",
    "Surabaya", "Bandung", "Medan", "Semarang"]

print("MAKE SURE WHEN YOU ANSWER ALWAYS WRITE JUST RAW NAME NOT WITH ANY COMMA OR PNUCTUATIONS FOR EX-> KABUL")

def chalukr():
    if(lai=='Y'):
        print("processing your choice")
        for i in range(4):
            ran=random.choices(non_capital_cities)
            lst1.append(ran)
        for l in range(1):
            ty=random.choices(list(capital_cities.keys()))
            lst1.append(ty)
        print("among this one is the capital",lst1)
        
        user_inp=input("enter the name which you think is capital city")
        if user_inp in non_capital_cities:
            print("sorry its a non capital city correct ans is",ty)

        else: 
            print("its a capital city")
    lst1.clear()


kloi=int(input("no of question to be asked"))
for i in range(1,kloi+1):
    chalukr()

    

    

