# Instructivo de cocina · Grupo la Independiente

Recorrido narrado de como se usan las fichas tecnicas: buscar una receta,
registrar la produccion del dia y leer el resumen del mes. Corre solo, con voz
y subtitulos, y sirve para los seis restaurantes.

**Es publico a proposito** y no lleva claves, costos ni recetas reales: las
pantallas son simuladas y estan marcadas como ejemplo. Por eso se puede mandar
por WhatsApp a cualquier cocina.

## Como se actualiza

La pagina se edita en la carpeta *Sistema v2 - fichas y produccion* y se arma
con `armar_instructivo.py`. Despues, `git push`: Railway redespliega solo.

| Archivo | Que es |
|---|---|
| `index.html` | La pagina completa. No se edita a mano. |
| `servidor.py` | Entrega la pagina. Sin variables ni configuracion. |
