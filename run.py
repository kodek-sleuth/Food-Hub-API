from app import create_app, db

app=create_app(config_name='testing')

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(port=3000)