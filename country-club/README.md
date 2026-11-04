# Hábitat Country Club

Landing independiente de los planes vacacionales (1 semana, 15 días, 1 mes).
No reemplaza la landing de Suramérica (`/index.html` en la raíz del repo).

## Subir a Hostinger
Sube **el contenido de esta carpeta** (`country-club/`) a la raíz del dominio o subdominio.
Todo lo que necesita está aquí: `index.html`, `gracias.html`, `politica.html`, `style.css`, logo, favicon e `img/`.

## Precios
Al final de `index.html`, en `PRECIOS_COP`, cambia `null` por el valor en pesos:

```js
const PRECIOS_COP = { semana: 3500000, quincena: 6500000, mes: 12000000 };
```

## Formulario y analítica
- Los leads van a la misma hoja de Suramérica (Apps Script actual) con
  `servicio = "Hábitat Country Club - Plan X"` y `fuente_lead = "Landing Hábitat Country Club"`.
- GTM: `GTM-WFSQ859`, con el evento `lead_country_club` al enviar.
- En vistas previas (githack, github.io, localhost, archivo local) no se carga GTM ni se envían leads.
