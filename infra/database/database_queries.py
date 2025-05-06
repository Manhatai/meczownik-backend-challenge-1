from fastapi import HTTPException

def query_multiple_items(database, model):
    return database.query(model).all()

def query_single_item(database, model, identifier, controller_name: str):
    item = database.query(model).filter(model.id == identifier).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"{controller_name} with id {identifier} not found [404]")
    return item

def add_and_commit(database, item):
    database.add(item)
    database.commit()
    database.refresh(item)
    return item

def delete_and_commit(database, item):
    database.delete(item)
    database.commit()
    return None