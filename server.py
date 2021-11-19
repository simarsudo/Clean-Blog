from flask import Flask, render_template, request
import smtplib


app = Flask(__name__)


response = [
    {
        "id": 0,
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
        "date": "9 July 2021",
        "title": "The Life of Cactus",
        "author": "Yuvraj",
        "subtitle": "Who knew that cacti lived such interesting lives."
    },
    {
        "id": 1,
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
        "date": "9 July 2021",
        "title": "Top 15 Things to do When You are Bored",
        "author": "Elder",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities."
    },
    {
        "id": 2,
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
        "date": "9 July 2021",
        "title": "Introduction to Intermittent Fasting",
        "author": "Mvj",
        "subtitle": "Learn about the newest health craze."
    }
]


@app.route("/")
def home():
    return render_template("index.html", posts=response)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name_ = data["name"]
        email_ = data["email"]
        phone_ = data["phone"]
        message_ = data["message"]

        my_email = "testmailthecoder@gmail.com"
        my_password = "testmail@123"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="sjthecoder@gmail.com", msg=f"Subject: Message from a fan\n\nName: {name_}\nEmail: {email_}\nPhone: {phone_}\nMessage: {message_}")

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/about-me")
def about():
    return render_template("about.html")


@app.route("/post/<int:value>")
def post(value):
    return render_template("post.html", id=value, posts=response)


if __name__ == "__main__":
    app.run(debug=True)
