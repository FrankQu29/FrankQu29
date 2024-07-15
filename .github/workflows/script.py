import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Reemplaza 'usuario' y 'repositorio' por el usuario y repositorio de GitHub deseado
url = 'https://api.github.com/repos/FrankQu29/FrankQU29/commits'
response = requests.get(url)
commits = response.json()

# Extraer las fechas de los commits
dates = [commit['commit']['committer']['date'] for commit in commits]

# Convertir las fechas a objetos datetime
dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') for date in dates]

# Contar commits por día
dates_count = {}
for date in dates:
    date_str = date.strftime('%Y-%m-%d')
    if date_str in dates_count:
        dates_count[date_str] += 1
    else:
        dates_count[date_str] = 1

# Ordenar las fechas
sorted_dates = sorted(dates_count.items())

# Separar las fechas y los conteos
dates, counts = zip(*sorted_dates)

# Generar la gráfica
plt.figure(figsize=(10, 5))
plt.plot(dates, counts)
plt.xlabel('Fecha')
plt.ylabel('Commits')
plt.title('Commits por día')
plt.grid(True)
plt.savefig('commits.png')

