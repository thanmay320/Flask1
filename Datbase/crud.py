from basic import db, Person, app
with app.app_context():
    # Fetching all Persons
    all_persons = Person.query.all()
    print(all_persons)

    # fetching with id
    ome_person=Person.query.get(1)
    print(ome_person)
    # filter
    x = Person.query.filter(Person.age > 20)
    print(x.all())
    # Update
    first_person=Person.query.get(1)
    first_person.age=25
    db.session.add(first_person)
    db.session.commit()
    # After Updation
    y = Person.query.filter(Person.age > 20)
    print(y.all())
    # deletion
    third_person=Person.query.get(3)
    db.session.delete(third_person)
    db.session.commit()

    #fetchng

    all=Person.query.all()
    print(all)




