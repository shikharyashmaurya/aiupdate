from flask import Flask,render_template
app=Flask(__name__)

new=[
    {
    "id":1,
    "title":"chat-gpt",
    "use":"give precise answer in human voice assisstant style"},
    {
    "id":2,
    "title":"dalle",
    "use":"generate image from the given text"
    }
    ]

@app.route("/")
def hello_world():
    return render_template("home.html",latest=new)

print(__name__)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)