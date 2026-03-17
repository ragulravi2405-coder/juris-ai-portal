from flask import Flask,request,redirect,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key="india_ai"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Abcd@1234'
app.config['MYSQL_DB']='juris_ai_portal'

mysql=MySQL(app)

# ---------------- HOME ----------------

@app.route('/')
def home():
    return redirect('/login')

# ---------------- REGISTER ----------------

@app.route('/register',methods=['GET','POST'])
def register():

    if request.method=='POST':

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",(name,email,password))
        mysql.connection.commit()

        return redirect('/login')

    return """

<html>

<style>

body{
background:linear-gradient(120deg,#FF9933,#FFFFFF);
font-family:Arial;
text-align:center;
}

form{
margin-top:120px;
background:white;
padding:40px;
display:inline-block;
border-radius:15px;
box-shadow:0px 5px 20px gray;
}

input{
padding:12px;
width:260px;
margin:10px;
border-radius:8px;
border:1px solid gray;
}

button{
padding:12px 25px;
background:#FF9933;
border:none;
border-radius:8px;
color:white;
font-size:16px;
cursor:pointer;
}

</style>

<body>

<h1>🇮🇳 Citizen Registration</h1>

<form method="POST">

<input name="name" placeholder="Full Name"><br>

<input name="email" placeholder="Email"><br>

<input name="password" placeholder="Password"><br>

<button>Register</button>

</form>

<br><br>

<a href="/login">Already have account? Login</a>

</body>

</html>

"""

# ---------------- LOGIN ----------------

@app.route('/login',methods=['GET','POST'])
def login():

    if request.method=='POST':

        email=request.form['email']
        password=request.form['password']

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",(email,password))

        user=cur.fetchone()

        if user:
            session['user']=user[1]
            return redirect('/dashboard')

    return """

<html>

<style>

body{
background:linear-gradient(120deg,#000080,#138808);
color:white;
font-family:Arial;
text-align:center;
}

form{
margin-top:130px;
background:white;
color:black;
padding:40px;
display:inline-block;
border-radius:15px;
}

input{
padding:12px;
width:260px;
margin:10px;
border-radius:8px;
border:1px solid gray;
}

button{
padding:12px 25px;
background:#000080;
border:none;
border-radius:8px;
color:white;
}

</style>

<body>

<h1>🇮🇳 Indian Legal AI Portal</h1>

<form method="POST">

<input name="email" placeholder="Email"><br>

<input name="password" placeholder="Password"><br>

<button>Login</button>

</form>

<br>

<a href="/register" style="color:white;">Create Account</a>

</body>

</html>

"""

# ---------------- DASHBOARD ----------------

@app.route('/dashboard')
def dashboard():

    return """

<html>

<style>

body{
background:#138808;
color:white;
text-align:center;
font-family:Arial;
}

.card{
display:inline-block;
background:white;
color:black;
padding:30px;
margin:25px;
width:220px;
border-radius:15px;
box-shadow:0px 4px 15px black;
transition:0.3s;
}

.card:hover{
transform:scale(1.1);
}

button{
padding:10px 20px;
background:#000080;
color:white;
border:none;
border-radius:8px;
}

</style>

<body>

<h1>Citizen Dashboard</h1>

<div class="card">

<h3>⚖ AI Legal Chat</h3>

<a href="/chat"><button>Open</button></a>

</div>

<div class="card">

<h3>📄 Complaint Portal</h3>

<a href="/complaint"><button>Open</button></a>

</div>

<div class="card">

<h3>📚 Constitution</h3>

<a href="/articles"><button>Open</button></a>

</div>

</body>

</html>

"""

# ---------------- AI CHAT ----------------

@app.route('/chat',methods=['GET','POST'])
def chat():

    answer="Ask about Indian law"

    if request.method=='POST':

        q=request.form['question'].lower()

        if "article 21" in q:
            answer="Article 21 – Right to Life and Personal Liberty"

        elif "article 14" in q:
            answer="Article 14 – Equality before law"

        elif "fir" in q:
            answer="FIR means First Information Report filed in police station"

        else:
            answer="Legal information not found"

    return f"""

<html>

<style>

body{{

background:#111827;
color:white;
text-align:center;
font-family:Arial;

}}

input{{

padding:12px;
width:350px;
border-radius:10px;
border:none;

}}

button{{

padding:10px 20px;
background:#FF9933;
border:none;
border-radius:10px;

}}

</style>

<body>

<h2>AI Legal Assistant</h2>

<form method="POST">

<input name="question" placeholder="Ask law question">

<button>Ask</button>

</form>

<h3>{answer}</h3>

</body>

</html>

"""

# ---------------- COMPLAINT ----------------

@app.route('/complaint',methods=['GET','POST'])
def complaint():

    if request.method=='POST':

        name=request.form['name']
        complaint=request.form['complaint']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO complaints(name,complaint) VALUES(%s,%s)",(name,complaint))
        mysql.connection.commit()

    return """

<html>

<style>

body{

background:#1e293b;
color:white;
text-align:center;
font-family:Arial;

}

textarea{

width:320px;
height:120px;
border-radius:10px;

}

button{

padding:10px 20px;
background:#138808;
border:none;
border-radius:10px;

}

</style>

<body>

<h2>Complaint Portal</h2>

<form method="POST">

<input name="name" placeholder="Name"><br><br>

<textarea name="complaint"></textarea><br><br>

<button>Submit Complaint</button>

</form>

</body>

</html>

"""

# ---------------- ARTICLES ----------------

@app.route('/articles')
def articles():

    return """

<html>

<style>

body{

background:#f3f4f6;
text-align:center;
font-family:Arial;

}

.card{

display:inline-block;
background:white;
padding:25px;
margin:20px;
width:200px;
border-radius:10px;
box-shadow:0px 4px 10px gray;

}

</style>

<body>

<h2>Indian Constitution Articles</h2>

<div class="card">Article 14</div>
<div class="card">Article 19</div>
<div class="card">Article 21</div>
<div class="card">Article 32</div>

</body>

</html>

"""

if __name__=="__main__":
    app.run(debug=True)