from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>User Info</title>
</head>
<body>
    <h2>Enter Your Details</h2>
    <form method="POST">
        Name: <input type="text" name="name"><br><br>
        Phone: <input type="text" name="phone"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        ip = request.remote_addr  # user ka IP (basic)

        with open("data.txt", "a") as f:
            f.write(f"Name: {name}, Phone: {phone}, IP: {ip}\n")

        return "Data saved successfully!"

    return render_template_string(html_form)

if __name__ == '__main__':
    app.run(debug=True)