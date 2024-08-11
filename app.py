from flask import Flask,request,render_template,Request,redirect,session
import test as m

app = Flask(__name__)

app.secret_key  = "my_secret_key"

users= {
    "imran":'1234'
}
@app.route("/")
def view_form():
    return render_template('login.html')

@app.route('/handel_get',methods=['GET'])
def handel_get():
    if request.method == 'GET':
        row_features ={"cap_shape" : request.args["cap-shape"],
        "cap_surface" : request.args["cap-surface"],
        "cap_color" : request.args["cap-color"],
        "oder" : request.args["odor"],
        "gill_attachment" : request.args["gill-attachment"],
        "gill_spacing" :request.args["gill-spacing"],
        "gill_size" : request.args["gill-size"],
        "gill_color" :request.args["gill-color"],
        "stalk_shape" : request.args["stalk-shape"],
        "stalk_root" : request.args["stalk-root"],
        "stalk_surface_above_ring" :request.args["stalk-surface-above-ring"],
        "stalk_surface_below_ring" : request.args["stalk-surface-below-ring"],
        "stalk_color_above_ring" : request.args["stalk-color-above-ring"],
        "stalk_color_below_ring" :request.args["stalk-color-below-ring"],
        "veil_type": request.args["veil-type"],
        "veil_color" : request.args["veil-color"],
        "ring_type" : request.args["ring-type"],
        "spore_print_color" : request.args["spore-print-color"],
        "population" :request.args["population"],
        "habitat" : request.args["habitat"],
        "bruises" : request.args["bruises"],
        "ring_number" :request.args["ring-number"]
        }
        result  = m.fun(row_features)
        
        return f"<h1>{result}</h1>"
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
