from pyepsilla import vectordb

## connect to vectordb
db = vectordb.Client(
  host='localhost',
  port='8888'
)

db.load_db(db_name="LocalChatDB", db_path="/tmp/epsilla")
db.use_db(db_name="LocalChatDB")

db.create_table(
  table_name="MyTable",
  table_fields=[
    {"name": "ID", "dataType": "INT", "primaryKey": True},
    {"name": "Doc", "dataType": "STRING"}
  ],
  indices=[
    {"name": "Index", "field": "Doc"}
  ]
)

db.insert(
  table_name="MyTable",
  records=[
    {"ID": 1, "Doc": "The garden was blooming with vibrant flowers, attracting butterflies and bees with their sweet nectar."},
    {"ID": 2, "Doc": "In the busy city streets, people rushed to and fro, hardly noticing the beauty of the day."},
    {"ID": 3, "Doc": "The library was a quiet haven, filled with the scent of old books and the soft rustling of pages."},
    {"ID": 4, "Doc": "High in the mountains, the air was crisp and clear, revealing breathtaking views of the valley below."},
    {"ID": 5, "Doc": "At the beach, children played joyfully in the sand, building castles and chasing the waves."},
    {"ID": 6, "Doc": "Deep in the forest, a deer cautiously stepped out, its ears alert for any signs of danger."},
    {"ID": 7, "Doc": "The old town's historical architecture spoke volumes about its rich cultural past."},
    {"ID": 8, "Doc": "Night fell, and the sky was a canvas of stars, shining brightly in the moon's soft glow."},
    {"ID": 9, "Doc": "A cozy cafe on the corner served the best hot chocolate, warming the hands and hearts of its visitors."},
    {"ID": 10, "Doc": "The artist's studio was cluttered but inspiring, filled with unfinished canvases and vibrant paints."}
  ]
)

status_code, response = db.query(
  table_name="MyTable",
  query_text="Where can I find a serene environment, ideal for relaxation and introspection?",
  limit=2
)
print(response)