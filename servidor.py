# -*- coding: utf-8 -*-
"""Sirve el instructivo de cocina. Una sola pagina, sin claves y sin datos:
el instructivo es publico a proposito, para poder mandarlo por WhatsApp.

Lo unico que hace es entregar index.html en cualquier direccion que pidan, con
el tipo de contenido correcto y sin guardar nada en cache: asi, cuando se
publique una version nueva, la cocina la ve al recargar.
"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

RAIZ = os.path.dirname(os.path.abspath(__file__))
PUERTO = int(os.environ.get("PORT", "8080"))
PAGINA = os.path.join(RAIZ, "index.html")


class Manejador(BaseHTTPRequestHandler):
    def _entregar(self, cuerpo, tipo="text/html; charset=utf-8", codigo=200):
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(cuerpo)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(cuerpo)

    def do_GET(self):
        if self.path == "/salud":
            return self._entregar(b"bien\n", "text/plain; charset=utf-8")
        try:
            with open(PAGINA, "rb") as fh:
                return self._entregar(fh.read())
        except OSError:
            return self._entregar(b"Falta index.html\n", "text/plain; charset=utf-8", 500)

    do_HEAD = do_GET

    def log_message(self, formato, *args):
        # Railway ya pone la hora delante de cada linea.
        print("%s - %s" % (self.address_string(), formato % args), flush=True)


if __name__ == "__main__":
    print("instructivo de cocina escuchando en el puerto %d" % PUERTO, flush=True)
    HTTPServer(("0.0.0.0", PUERTO), Manejador).serve_forever()
