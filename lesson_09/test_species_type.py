from species_type import Species_type

db = Species_type("postgresql://postgres:123456aA@localhost:5432/QA")


def test_create():
    db.create_species_type(8, "робот")

    assert db.get_species_type_by_id(db.create_id)[0]["type_name"]\
        == db.create_name

    db.delete_species_type(db.create_id)


def test_update():
    db.create_species_type(8, "робот")
    db.update_species_type(db.create_id, "андроид")

    assert db.get_species_type_by_id(db.existing_id)[0]["type_name"]\
        == db.new_name

    db.delete_species_type(db.existing_id)


def test_delete():
    db.create_species_type(8, "робот")
    db.delete_species_type(db.create_id)

    for each in db.get_species_type():
        assert ["type_id"] != db.create_id
    for each in db.get_species_type():
        assert ["type_name"] != db.create_name
