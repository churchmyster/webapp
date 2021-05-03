from website import app

# Desired port number
PORT = 3000

app = app()

if __name__ == '__main__':
    app.run(port=PORT, debug=True)