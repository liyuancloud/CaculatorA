import functions_framework
@functions_framework.http

def subtraction_http(request):
    
    """HTTP Cloud Function.
    Args:
        a  - the a value
        b  - the b value
    Returns:
        The computed value
    """
    
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    return f"The result of subtraction is: subtraction(a,b)"

def subtraction(a,b):
    return a - b
