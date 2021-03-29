from music_app import create_app

# Create the application 
app = create_app()

# Driver code
if __name__ == '__main__':
    app.run(debug=True)