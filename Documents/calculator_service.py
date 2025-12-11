from spyne import Application, rpc, ServiceBase, Integer, Float, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.serving import run_simple


class CalculatorService(ServiceBase):

    @rpc(Float, Float, _returns=Float)
    def add(ctx, a, b):
        return a + b

    @rpc(Float, Float, _returns=Float)
    def subtract(ctx, a, b):
        return a - b

    @rpc(Float, Float, _returns=Float)
    def multiply(ctx, a, b):
        return a * b

    @rpc(Float, Float, _returns=Float)
    def divide(ctx, a, b):
        if b == 0:
            return 0
        return a / b


# SOAP Application settings
soap_app = Application(
    [CalculatorService],
    tns='calculator.soap.service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)


if __name__ == '__main__':
    print("SOAP Calculator Service Running...")
    print("WSDL URL: http://localhost:8000/?wsdl")
    run_simple("0.0.0.0", 8000, wsgi_app)
