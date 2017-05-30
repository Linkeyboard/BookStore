from flask import Flask


app = Flask(__name__)


app.secret_key = "T2tFqZcOUO8uv5zcG9rFkUKi0ziFOhBSWYmzy8DO"

import BookStore.views
import BookStore.database