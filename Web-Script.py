from flask import Flask , render_template
from forms import RigistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '57c2987f11eaf607c560bfe1752403a98f3906d46d371565da92f7b76318687a'

certificat_experiences =[{
    'title':'certificat ccna2',
    'description':'Notions de base sur la commutation, le routage et le sans fil',
    'icon':'certificat_ccna2.PNG'
},
{
    'title':'CCNA badge',
    'description':'CCNA: Switching, Routing, and Wireless Essentials',
    'icon':'badge_ccna.PNG'
}]

my_script = [{
    'title':'script scan network',
    'description':'script  scan Network',
    'author':'houssam',
    'icon':'Network.png'
},
{
    'title':'script Dino T-Rex',
    'description':'In order to get a record in the game',
    'author':'houssam',
    'icon':'DINO_game.PNG'
},
{
    'title':'login page',
    'description':'login page professional',
    'author':'fariss',
    'icon':'web.png'
}
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", my_script=my_script, certificat_experiences=certificat_experiences, title_head = "home page" )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    form = RigistrationForm()
    return render_template("register.html", title = "register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "login", form = form)

if __name__=="__main__":
    app.run(debug=True, port=7000)
