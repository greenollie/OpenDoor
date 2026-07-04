@mcp.tool()
def get_weather(forecast_days: int = 1) -> str:
    """Get the weather forecast in the user's set location for a specific number of days.
    
    Args:
        forecast_days: The number of days to look ahead. Use 1 for today, 2 to include tomorrow, or 7 for the entire upcoming week.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": ["temperature_2m"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "weather_code"],
        "forecast_days": forecast_days,
        "timezone": "auto"
    }
    response = requests.get(url, params=params).json()
    current_temp = response["current"]["temperature_2m"]
    daily = response["daily"]
    wmo_codes = {
        0: "completely clear skies",
        1: "mainly clear skies", 2: "partly cloudy conditions", 3: "overcast skies",
        45: "foggy conditions", 48: "depositing rime fog",
        51: "a possible light drizzle", 53: "moderate drizzle", 55: "dense drizzle",
        61: "slight rain", 63: "moderate rain", 65: "heavy rain",
        80: "slight rain showers", 81: "moderate rain showers", 95: "a thunderstorm"
    }
    output_lines = []
    for i in range(len(daily["time"])):
        date_str = daily["time"][i]
        max_temp = daily["temperature_2m_max"][i]
        min_min = daily["temperature_2m_min"][i]
        rain = daily["precipitation_sum"][i]
        code = daily["weather_code"][i]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        weekday = date_obj.strftime("%A")
        condition = wmo_codes.get(code, "unpredictable weather conditions")
        rain_phrase = "with no rain expected." if rain < 0.1 else f"with {rain}mm of rain."
        today = datetime.now().date()
        if date_str == today.strftime("%Y-%m-%d"):
            output_lines.append(
                f"Right now on {weekday}, it is currently {current_temp}°C. Expect {condition} with temperatures reaching a high of {max_temp}°C "
                f"and a low of {min_min}°C, {rain_phrase}"
            )
        else:
            output_lines.append(
                f"For {weekday}, {date_str}: Expect {condition} with temperatures reaching a high of {max_temp}°C "
                f"and a low of {min_min}°C, {rain_phrase}"
            )
    forecast_paragraph = (
        "Give the user this information in a readable format, like a friendly charismatic weather person:\nMake sure to detect trends thoughout the amount of time and try to summerise the information.\nExample: \"Right now, it is currently 23°C. Expect a possible shower with temperatures reaching a high of 25°C and a low of 20°C, with no rain expected. Over the next few days you can expect increasing temperature with a high of 32°C.\nThe user expects a very brief summery of alot of information. Make it quick.\nDo not make your response a list. Have it flow like with a weather report on the news.\nOnly talk fully about 1-2 days, summerise the rest, talk about a general increase or decrease, etc.\n\n"
        + "\n".join(output_lines)
    )
    return forecast_paragraph
