whether={"city": "Москва", "temperature": 20}
print(whether)
print(whether["city"])
print(whether["temperature"])

whether["temperature"] -=5
print(whether["temperature"])
print(whether)
print(whether.get("country", 'Russia'))
whether["date"] = "27.05.2019"
print(whether)
print(len(whether))