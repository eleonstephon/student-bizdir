from flask import Flask, request, render_template_string

app = Flask(__name__)

# This is a simple HTML form written directly in Python
# (normally Member 1 would write this in a separate HTML file)
FORM_HTML = """
<!DOCTYPE html>
<html>
<head><title>Test Form</title></head>
<body>
    <h1>Test Form</h1>

    <!-- This form sends data to /submit when clicked -->
    <form action="/submit" method="POST">
        <label>Your Name:</label><br>
        <input type="text" name="name"><br><br>

        <label>Your Email:</label><br>
        <input type="text" name="email"><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Show the form
@app.route("/")
def show_form():
    return render_template_string(FORM_HTML)

# Receive the form data and display it back
@app.route("/submit", methods=["POST"])
def submit():
    name  = request.form.get("name")
    email = request.form.get("email")
    return f"<h1>Hello {name}!</h1><p>Your email is: {email}</p>"

if __name__ == "__main__":
    app.run(debug=True)