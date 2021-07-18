import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.040987  # Your latitude
MY_LONG = 100.614597  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login("chutayu.adhi@gmail.com", "Kiss7468")
            connection.sendmail(
                from_addr="chutayu.adhi@gmail.com",
                to_addrs="chutayu.adhi@bumail.net",
                msg="Subject:ISS Now here!✨\n\nGo to see Bro.The ISS is above you in the sky."
            )
    else:
        print("Not now Bro")
