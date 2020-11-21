from flask import Flask, render_template, redirect, url_for, request

app = Flask (__name__)

@app.route('/')
def index():
  return render_template('helloWorld.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/dynamic')
def dynamic():
  greeting = "What's good"
  name = "Thalia"
  favoriteMovies = ["Tombstone", "Star Wars: Empire Strikes Back", 
  "Catch Me if You Can"]

  return render_template('dynamic.html', greeting=greeting, name=name, favoriteMovies=favoriteMovies)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')