from sqlalchemy.orm import Session
import models


def create_michelin_guide_data(
    db: Session, michelin_guide_data: models.MichelinGuideData
) -> models.MichelinGuideData:
    db_michelin_guide = models.MichelinGuideData(**michelin_guide_data)
    db.add(db_michelin_guide)
    db.commit()
    db.refresh(db_michelin_guide)
    return db_michelin_guide


def get_michelin_guide_data(db: Session):
    return db.query(models.MichelinGuideData).offset(0).limit(100).all()
