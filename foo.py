from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import select
from sqlalchemy.orm import declarative_base, Session


BASE = declarative_base()


class Message(BASE):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    message = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f'Message(id={self.id!r}, message={self.message!r})'


def main():
    engine = create_engine('mysql://user:pass@127.0.0.1:33061/demo', echo=True)
    BASE.metadata.create_all(engine)

    with Session(engine) as session:
        message_a = Message(message="hello, world")
        session.add(message_a)
        session.commit()

    session = Session(engine)
    for message in session.scalars(select(Message)):
        print(message)


if __name__ == '__main__':
    main()
