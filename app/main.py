"""Main Flask application."""
from flask import Flask
from flask_restx import Api, Resource, fields

from app.services.dictionary_service import Dictionary
from app.services.spend_service import get_total
from app.services.word_service import build_word

app = Flask(__name__)

api = Api(
    app,
    title="Python DevOps Lab API",
    version="1.0",
    description="API para las tareas del PDF usando Flask y Swagger",
    doc="/swagger"
)

dictionary_ns = api.namespace("dictionary", description="Dictionary operations")
spend_ns = api.namespace("spend", description="Spend calculator")
word_ns = api.namespace("word", description="Word builder")

dictionary = Dictionary()

dictionary_model = api.model("DictionaryEntry", {
    "word": fields.String(required=True, example="Apple"),
    "definition": fields.String(required=True, example="A fruit that grows on trees")
})

spend_model = api.model("SpendRequest", {
    "costs": fields.Raw(required=True, example={
        "socks": 5,
        "shoes": 60,
        "sweater": 30
    }),
    "items": fields.List(fields.String, required=True, example=["socks", "shoes"]),
    "tax": fields.Float(required=True, example=0.09)
})

word_model = api.model("WordRequest", {
    "words": fields.List(fields.String, required=True, example=["yoda", "best", "has"])
})


@dictionary_ns.route("/")
class DictionaryEntryResource(Resource):
    """Dictionary entry resource."""

    @dictionary_ns.expect(dictionary_model)
    def post(self):
        """Create dictionary entry."""
        data = api.payload
        dictionary.newentry(data["word"], data["definition"])
        return {"message": "Entry added successfully"}, 201

@dictionary_ns.route("/<string:word>")
class DictionaryLookupResource(Resource):
    """Dictionary lookup resource."""

    def get(self, word):
        """Get dictionary entry by word."""
        result = dictionary.look(word)
        return {"result": result}, 200

@spend_ns.route("/")
class SpendResource(Resource):
    """Spend resource."""


    @spend_ns.expect(spend_model)
    def post(self):
        """Calculate total cost from request."""
        data = api.payload
        total = get_total(data["costs"], data["items"], data["tax"])
        return {"total": total}, 200

@word_ns.route("/")
class WordResource(Resource):
    """Word resource."""
    @word_ns.expect(word_model)
    def post(self):
        """Build word from request."""
        data = api.payload
        result = build_word(data["words"])
        return {"result": result}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # nosec B104

