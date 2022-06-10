from db.run_sql import run_sql
from models.publisher import Publisher

def save(publisher):
  sql = "INSERT INTO publishers(name, address, phone_number) VALUES ( %s, %s, %s) RETURNING id"
  values = [publisher.name, publisher.address, publisher.phone_number]
  results = run_sql(sql, values)
  publisher.id = results[0]['id']
  return publisher

def select_all():
  publishers = []
  sql = "SELECT * FROM publishers"
  results = run_sql(sql)
  for row in results:
    publisher = Publisher(row["name"], row["address"], row["phone_number"], row["id"])
    publishers.append(publisher)
  return publishers

def select(id):
  publisher = None
  sql = "SELECT * FROM publishers WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  if result is not None:
    publisher = Publisher(result["name"], result["address"], result["phone_number"], result["id"])
  return publisher

def delete(id):
  sql = "DELETE FROM publishers WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def delete_all():
  sql = "DELETE FROM publishers"
  run_sql(sql)