import streamlit as st


def convert_unit(value, convert_from, convert_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "celsius_fahrenheit": lambda c: (c * 9 / 5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5 / 9,
        "celsius_kelvin": lambda c: c + 273.15,
        "kelvin_celsius": lambda k: k - 273.15,
        "liter_milliliter": 1000,
        "milliliter_liter": 0.001,
    }

    key = f"{convert_from}_{convert_to}"

    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion Not Supported"


st.title("Unit Converter")


value = st.number_input("Enter the Value:", min_value=1.0, step=1.0)
category = st.selectbox(
    "Select Conversion Category:", ["Length", "Weight", "Temperature", "Volume"]
)


unit_options = {
    "Length": ["meter", "kilometer"],
    "Weight": ["gram", "kilogram"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter"],
}

convert_from = st.selectbox("Convert From:", unit_options[category])
convert_to = st.selectbox("Convert To:", unit_options[category])


if st.button("Convert"):
    result = convert_unit(value, convert_from, convert_to)
    st.success(f"Converted Value: {result} {convert_to}")
