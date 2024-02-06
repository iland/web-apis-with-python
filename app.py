from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/search")
def search():
    args = request.args.get("q")
    submit = request.args.get("submit")
    
    if "search" == submit:
        return redirect(f"https://google.com/search?q={args}")
    elif "lucky" == submit:
        # TODO Need to improve
        return redirect(f"https://www.google.com/search?q={args}&btnI=I'm+Feeling+Lucky")
    else:
        return redirect("/");

if __name__ == "__main__":
    app.run()