from flask import Flask, render_template,request,jsonify,redirect,url_for
import pickle
import pandas as pd
import sklearn
from flask_cors import cross_origin
app = Flask(__name__)
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open("Model1low_memory.pkl", "rb"))

#@app.route('/')

#def home():
    #return render_template('home.html')

@app.route('/',methods=['GET','POST'])

def predict():
    if request.method=='POST':


        airline=request.form['airline']
        if(airline=='SpiceJet'):
            SpiceJet=4


        elif(airline=='AirAsia'):
            AirAsia=0
        elif(airline=='Vistara'):
            Vistara=5
        elif(airline=='GO_FIRST'):
            GO_FIRST=2
        elif(airline=='Indigo'):
            Indigo=3
        elif(airline=='Air_India'):
            Air_India=1

        Departure_time=request.form['Departure time']
        if(Departure_time=='Evening'):
            Evening=2

        elif (Departure_time == 'Early_Morning'):
            Early_Morning = 1

        elif (Departure_time == 'Morning'):
            Morning = 4

        elif (Departure_time == 'Afternoon'):
            Afternoon = 0

        elif (Departure_time == 'Night'):
            Night = 5

        elif (Departure_time == 'Late_Night'):
            Late_Night = 3
        source_city=request.form['source_city']
        if (source_city=='Delhi'):
            Delhi=2

        elif (source_city=='Mumbai'):
            Mumbai=5

        elif (source_city=='Bangalore'):
            Bangalore=0

        elif (source_city=='Kolkata'):
            Kolkata=4

        elif (source_city=='Hyderabad'):
            Hyderabad=3

        elif (source_city=='Chennai'):
            Chennai=1
        destination_city=request.form['destination_city']

        if (destination_city == 'Mumbai'):
            Mumbai = 5

        elif (destination_city == 'Bangalore'):
            Bangalore =0

        elif (destination_city == 'Kolkata'):
            Kolkata = 4

        elif (destination_city == 'Hyderabad'):
            Hyderabad = 3

        elif (destination_city == 'Chennai'):

            Chennai = 1
        elif (destination_city == 'Delhi'):


            Delhi = 2


        stops=request.form['stops']
        if (stops == 'zero'):
            zero = 2

        elif (stops == 'one'):
            one = 0

        elif (stops == 'two_or_more'):
            two_or_more = 1

        arrival_time=request.form['arrival_time']
        if(arrival_time=='Night'):
            Night = 5

        elif (arrival_time == 'Morning'):
            Morning=4

        elif (arrival_time == 'Early_Morning'):
            Early_Morning =1

        elif (arrival_time == 'Afternoon'):
            Afternoon=0

        elif (arrival_time == 'Evening'):
            Evening=2


        elif (arrival_time == 'Late_Night'):
            Late_Night=3
        classs=request.form['Class']
        if (classs == 'Economy'):
            Economy = 1
        elif (classs == 'Business'):
            Business = 0
        days_left=int(request.form['days_left'])
        Du_hour = int(request.form['Du_hour'])
        Du_min = int(request.form['Du_min'])

        print(airline)
        prediction = model.predict([[
            airline,
            source_city,
            Departure_time,
            stops,
            arrival_time,
            destination_city,
            classs,
            days_left,
            Du_hour,
            Du_min

        ]])
        output = int(prediction)
        print(output)
        return redirect(url_for('result', output=output))
        #return render_template('home.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")
@app.route('/result')
def result():
    output=request.args.get('output',None)
    return render_template('result.html',output=output)
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()