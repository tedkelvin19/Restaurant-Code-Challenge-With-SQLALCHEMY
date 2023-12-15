from sqlalchemy import create_engine,text

engine = create_engine('sqlite:///restaurant.db',echo=True)

with engine.connect() as conn:
    result = conn.execute(text('select"Connected to databse"'))
    
    print(result.all())