champions = {
    "Alistar": "sup",
    "Braum": "sup",
    "Leona": "sup",
    "Ornn": "top",
    "Master Yi": "jungle",
    "Sejuani": "top",
    "Shen": "top",
    "Katarina": "mid",
    "Tristana": "adc",
    "Rell": "sup"
}

champions["Lux"] = "sup"
del champions["Lux"]

for champion in champions:
    print(f"Champion: {champion} - Route: {champions[champion]}")


print("Rell" in champions)
print("Rakan" in champions)
