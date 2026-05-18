# save this file as app.py
# run with:
# pip install flask
# python app.py

from flask import Flask, render_template_string

app = Flask(__name__)

# Common HTML Template
def page_template(title, message, yes_link, no_link=None, disable_no=False):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>

        <style>
            body {{
                margin: 0;
                padding: 0;
                height: 100vh;
                overflow: hidden;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #ffb6c1, #ffe4e1);
            }}

            .container {{
                text-align: center;
                background: rgba(255,255,255,0.2);
                padding: 40px;
                border-radius: 25px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 20px rgba(0,0,0,0.2);
                position: relative;
                z-index: 2;
            }}

            h1 {{
                color: #ff1493;
                font-size: 40px;
                margin-bottom: 20px;
            }}

            img {{
                width: 220px;
                border-radius: 20px;
                margin-bottom: 20px;
            }}

            .btn {{
                text-decoration: none;
                padding: 12px 30px;
                margin: 10px;
                border-radius: 50px;
                font-size: 20px;
                font-weight: bold;
                transition: 0.3s;
                display: inline-block;
            }}

            .yes {{
                background: #ff1493;
                color: white;
            }}

            .yes:hover {{
                transform: scale(1.1);
                background: #ff69b4;
            }}

            .no {{
                background: white;
                color: #ff1493;
            }}

            .no:hover {{
                transform: scale(1.1);
            }}

            .disabled {{
                pointer-events: none;
                opacity: 0.5;
            }}

            /* Watermark */
            .watermark {{
                position: absolute;
                top: 15px;
                left: 20px;
                color: white;
                font-size: 18px;
                font-weight: bold;
                opacity: 0.85;
                z-index: 999;
                text-shadow: 0 0 10px rgba(0,0,0,0.4);
            }}

            /* Heart Animation */
            .heart {{
                position: absolute;
                color: red;
                font-size: 24px;
                animation: float 6s linear infinite;
            }}

            @keyframes float {{
                0% {{
                    transform: translateY(100vh) scale(0);
                    opacity: 0;
                }}
                50% {{
                    opacity: 1;
                }}
                100% {{
                    transform: translateY(-10vh) scale(1.5);
                    opacity: 0;
                }}
            }}
        </style>
    </head>

    <body>

        <!-- Watermark -->
        <div class="watermark">Made By Eqlipse ✨</div>

        <!-- Floating Hearts -->
        <script>
            function createHeart() {{
                const heart = document.createElement('div');
                heart.classList.add('heart');
                heart.innerHTML = '❤';

                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.animationDuration = (Math.random() * 3 + 3) + 's';
                heart.style.fontSize = (Math.random() * 20 + 20) + 'px';

                document.body.appendChild(heart);

                setTimeout(() => {{
                    heart.remove();
                }}, 6000);
            }}

            setInterval(createHeart, 300);
        </script>

        <div class="container">

            <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">

            <h1>{message}</h1>

            <a class="btn yes" href="{yes_link}">Yes 💖</a>

            {"<a class='btn no disabled'>No 💔</a>" if disable_no else (f"<a class='btn no' href='{no_link}'>No 💔</a>" if no_link else "")}

        </div>

    </body>
    </html>
    """


@app.route("/")
def home():
    return render_template_string(
        page_template(
            "Love Question",
            "Do you like me or not? as a friend!!! 🥺",
            "/yes",
            "/think"
        )
    )


@app.route("/think")
def think():
    return render_template_string(
        page_template(
            "Think Again",
            "Think again 😭",
            "/yes",
            "/sure"
        )
    )


@app.route("/sure")
def sure():
    return render_template_string(
        page_template(
            "Are You Sure?",
            "Are you really sure? 😢",
            "/yes",
            "/final"
        )
    )


@app.route("/final")
def final():
    return render_template_string(
        page_template(
            "No Escape",
            "Now you only have one option 😎",
            "/yes",
            disable_no=True
        )
    )


@app.route("/yes")
def yes():
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Yayyy</title>

            <style>
                body {
                    margin: 0;
                    padding: 0;
                    height: 100vh;
                    overflow: hidden;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: linear-gradient(135deg, #ff69b4, #ff1493);
                    font-family: Arial, sans-serif;
                }

                .container {
                    text-align: center;
                    color: white;
                }

                h1 {
                    font-size: 60px;
                    animation: pulse 1s infinite;
                }

                img {
                    width: 280px;
                    border-radius: 20px;
                }

                /* Watermark */
                .watermark {
                    position: absolute;
                    top: 15px;
                    left: 20px;
                    color: white;
                    font-size: 18px;
                    font-weight: bold;
                    opacity: 0.85;
                    z-index: 999;
                    text-shadow: 0 0 10px rgba(0,0,0,0.4);
                }

                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.1); }
                    100% { transform: scale(1); }
                }

                .heart {
                    position: absolute;
                    color: white;
                    font-size: 24px;
                    animation: float 5s linear infinite;
                }

                @keyframes float {
                    0% {
                        transform: translateY(100vh) scale(0);
                        opacity: 0;
                    }
                    50% {
                        opacity: 1;
                    }
                    100% {
                        transform: translateY(-10vh) scale(1.5);
                        opacity: 0;
                    }
                }
            </style>
        </head>

        <body>

            <!-- Watermark -->
            <div class="watermark">Made By Eqlipse ✨</div>

            <script>
                function createHeart() {
                    const heart = document.createElement('div');
                    heart.classList.add('heart');
                    heart.innerHTML = '❤';

                    heart.style.left = Math.random() * 100 + 'vw';
                    heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
                    heart.style.fontSize = (Math.random() * 20 + 20) + 'px';

                    document.body.appendChild(heart);

                    setTimeout(() => {
                        heart.remove();
                    }, 5000);
                }

                setInterval(createHeart, 200);
            </script>

            <div class="container">

                <img src="https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif">

                <h1>I knew that AMINA 💖🐼</h1>

            </div>

        </body>
        </html>
        """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)