from portfolio_koch.wsgi import application

def handler(request, context):
    return application(request)