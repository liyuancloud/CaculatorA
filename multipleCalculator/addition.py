import functions_framework
@functions_framework.http
def addition_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    return f"The result of addition is: {addition(a,b)}"

def addition(a,b):
    return a+b