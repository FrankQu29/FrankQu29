# FrankQu
### Hey everybody I'm Francisco: an aeronautical engineering student and a jr-dev

---
- I'm interested in aerospatial engineering
- I'd like to improve my developer skills
---

## Ejemplo de Gráfica en R

Para ejecutar este ejemplo, asegúrate de tener instalado R y el paquete `ggplot2`.

### Código R

```R
# Instala ggplot2 si no está instalado
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

# Carga la librería ggplot2
library(ggplot2)

# Genera datos de ejemplo
set.seed(123)
datos <- data.frame(
  x = rnorm(100),
  y = rnorm(100)
)

# Crea un gráfico de dispersión
grafico <- ggplot(datos, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Gráfico de Dispersión", x = "Eje X", y = "Eje Y")

# Muestra el gráfico
print(grafico)
