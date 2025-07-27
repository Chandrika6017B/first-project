from flask import Flask, render_template_string

app = Flask(__name__)

html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #222;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            margin-top: 10px;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 10px;
        }
        main {
            padding: 20px;
        }
        section {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        footer {
            background-color: #222;
            color: white;
            text-align: center;
            padding: 15px;
        }
        a {
            color: #0066cc;
        }
    </style>
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
        <nav>
            <a href="/">Home</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>About Me</h2>
            <p>I am an IoT student with knowledge in Python and Web Development. I enjoy building smart and useful applications.</p>
        </section>

        <section>
            <h2>Projects</h2>
            <ul>
                <li><strong>SmartSDLC:</strong> AI-based SDLC automation platform</li>
                <li><strong>E-Commerce Website:</strong> Online product page using web development</li>
                <li><strong>Saline Monitoring System:</strong> IoT project using buzzer alert for empty saline</li>
            </ul>
        </section>

        <section>
            <h2>Contact</h2>
            <p>Email: your.email@example.com</p>
            <p>LinkedIn: <a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Your Name</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
