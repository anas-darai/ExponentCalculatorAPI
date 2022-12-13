from server import app


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')


@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')



from flask import request,jsonify

@app.route('/calcPower', methods=['GET'])
def calcPower():
    args = request.args
    x = args.get("x", default=1, type=int)
    y = args.get("y", default=1, type=int)
    
    response = jsonify({"result": str(x**y)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
