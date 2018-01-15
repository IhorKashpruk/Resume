from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/css')
@app.route('/font-ukie')
@app.route('/font-ukie/css')
@app.route('/font-ukie/fonts')
@app.route('/images')
@app.route('/__MACOS')
@app.route('/__MACOS/font-ukie')
@app.route('/__MACOS/font-ukie/css')
@app.route('/__MACOS/font-ukie/fonts')
def index():
  return "index"

if __name__ == '__main__':
  app.run()
