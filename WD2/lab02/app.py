from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/spy", methods=["GET", "POST"])
def introduction():
    if request.method == "GET":
        return render_template("form.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("response.html", family_name=family_name, given_name=given_name)

@app.route("/morse", methods=["GET", "POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        morse = ""
        morse_dict= {'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..',
                        'E':'.', 'F': '..-.',
                        'G':'--.', 'H':'--.',
                        'I':'..','J':'.---',
                        'K':'-.-','L':'.-..',
                        'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.',
                        'Q':'--.-', 'R':'.-.',
                        'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 
                        'W':'.--', 'X':'-..-',
                        'Y':'-.--', 'Z':'--..',
                        " ":'/'
                    }
        for char in message:
            char = char.capitalize()
            if char in morse_dict.keys():
                code = morse_dict[char]
                morse = morse + code + " "
            else:
                return render_template("morse_form.html", message="", morse="", error="A message is required!")
        if message == "":
            return render_template("morse_form.html", message="", morse="", error="A message is required!")
        return render_template("morse_response.html", morse=morse, message=message)


@app.route("/lenghts", methods=["GET", "POST"])
def introduction2():
    if request.method == "GET":
        return render_template("form2.html")
    else:
        inches = request.form["inches"]
        centimetres = request.form["centimetres"]
        inches_flag = 0
        centimetres_flag = 0
        if inches != "":
            inches_flag = 1
        if centimetres != "":
            centimetres_flag = 1
        if centimetres_flag and inches_flag == 1:
            return render_template("form2.html", error="Please fill in one textfield.")
        if centimetres_flag == 1:
            centimetres = float(centimetres)
            inches = centimetres / 2.54
            return render_template("size_response.html", centimetres=centimetres, inches=inches)
        elif inches_flag == 1:
            inches = float(inches)
            centimetres = inches * 2.54
            return render_template("size_response.html", centimetres=centimetres, inches=inches)
        if centimetres_flag or inches_flag == 0:
            return render_template("form2.html", error="Please fill in one textfield.")
        return render_template("size_response.html", centimetres=centimetres, inches=inches)



