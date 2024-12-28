from sqlalchemy.orm import Session
from app.models import Item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: Item):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
