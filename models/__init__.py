def setup_db(app):
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy.orm import DeclarativeBase

    host= '192.168.0.201'
    database= 'diana'
    user= 'diana'
    password= 'Diana1234'
    string_conn = f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'
    app.config["SQLALCHEMY_DATABASE_URI"] = string_conn

    class Base(DeclarativeBase):
        pass

    db = SQLAlchemy(model_class=Base)

    return db
