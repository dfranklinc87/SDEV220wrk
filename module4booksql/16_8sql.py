import sqlalchemy as sa
from sqlalchemy import text


engine = sa.create_engine('sqlite:///book.sqlite')

with engine.connect() as conn:
  rows = conn.execute(text('select title from book order by title'))
  for row in rows:
    print(row.title)

