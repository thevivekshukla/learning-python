from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import pandas
from geopy.geocoders import Nominatim
from datetime import datetime

nom = Nominatim(timeout=10)

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
  global filename
  if request.method == 'POST':
    file = request.files["file"]

    try:
      df = pandas.read_csv(file)
      if "Address" in df.columns:
        df["coordinates"] = df["Address"].apply(nom.geocode)
        df["latitude"] = df["coordinates"].apply(lambda x: x.latitude if x!=None else None)
        df["longitude"] = df["coordinates"].apply(lambda x: x.longitude if x!=None else None)
        df = df.drop("coordinates", 1)
        filename = datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f"+".csv")
        df.to_csv(filename)

        return render_template("index.html", df=df.to_html(), btn="download.html")
      else:
        return render_template("index.html", message="file should have column named 'Address'.")
    except:
      pass


  return render_template("index.html", message="Some error has occured.")


@app.route('/download')
def download():
  return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
  app.run(debug=True)
