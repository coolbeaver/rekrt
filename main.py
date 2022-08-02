from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():
    args = request.args
    name = args.get("name", default="")
    message = args.get("message", default="")
    return f"Hello {name}! {message}"


if __name__ == "__main__":
    app.run()
