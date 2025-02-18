from basic import db, Person, app
with app.app_context():
    db.create_all()

    # Create Person objects
    thanmay = Person('thanmay', 20)
    rao = Person('rao', 21)
#insert all
    db.session.add_all([thanmay, rao])
    db.session.commit()
#insert
    manjith=Person('manjith',23)
    db.session.add(manjith)
    db.session.commit()
