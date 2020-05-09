
import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from spyne.model.primitive import String
from spyne.model.primitive import Boolean, Unicode, Integer
from spyne.model.complex import ComplexModel
from itertools import cycle

class MyHeader(ComplexModel):
   info = Unicode
class Validation(Unicode):
    @staticmethod
    def checkInput(inputString):
        return any(char.isdigit() for char in inputString)

class verificaRutService(ServiceBase):
    __in_header__ = MyHeader

    @rpc(Unicode, _returns = Iterable(Unicode))
    def verificarut(ctx, rut):
        rut1 = rut
        rut1 = rut1.replace(".", "")
        rut1 = rut1.replace("-", "")

        aux = rut1[:-1]
        dv = rut1[-1:]

        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s)%11

        if str(res) == dv:
            msj = "El Rut ingresado " + rut + " es valido, el digito verificador es "+ dv
            yield msj
        elif dv == "K" and res==10:
            msj = "El Rut ingresado " + rut + " es valido, el digito verificador es "+ dv
            yield msj
        else:
            msj = "El Rut ingresado " + rut + " es invalido"
            yield msj

class nombreTituloService(ServiceBase):
    __in_header__ = MyHeader
    ValidationClass = Validation
    @rpc(Unicode,Unicode,Unicode,Unicode, _returns = Iterable(Unicode))
    def nombretitulo(ctx,name,apellido_paterno,apellido_materno,gender):
        validate=1
        arrayInput = [
            name,
            apellido_paterno,
            apellido_materno,
            gender
        ]
        for i in arrayInput:
            if (Validation.checkInput(i)):
                validate=0
        if (validate==1):
            if (gender in ('M','m','f','F')):
                if gender=='M' or gender=='m':
                    gender='Sr.'
                elif gender=='F' or gender=='f':
                    gender='Sra.'
                nombrecompleto = gender + ' ' + name + ' ' + apellido_paterno + ' ' + apellido_materno
                msj = 'Hola ' + nombrecompleto.title()
                yield msj
            else:
                msj = 'El genero no coincide con lo permitido, ingrese (M,F,m,f)'
                yield msj
        else:
            msj = 'No se permiten caracteres a excepcion de letras en los nombres'
            yield msj

application = Application([
        verificaRutService,
        nombreTituloService
    ],
    tns='/',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
