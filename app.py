from flask import Flask, render_template, request
from urllib.parse import quote

app = Flask(__name__)

# IMPORTANT: Replace this with your WhatsApp number, including country code.
# India example: 919876543210 (no +, spaces, or dashes)
WHATSAPP_NUMBER = "919000000000"

DESIGNS = [
    {
        "title": "Gold Elite Jersey",
        "category": "Jersey Design",
        "description": "A premium black-and-gold sports look.",
        "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=1000&q=85",
    },
    {
        "title": "Team Match Kit",
        "category": "Jersey Design",
        "description": "Bold match-day styling for your team.",
        "image": "https://images.unsplash.com/photo-1517466787929-bc90951d0974?auto=format&fit=crop&w=1000&q=85",
    },
    {
        "title": "Brand Identity",
        "category": "Logo & Branding",
        "description": "Distinctive visual direction for a brand.",
        "image": "https://images.unsplash.com/photo-1626785774573-4b799315345d?auto=format&fit=crop&w=1000&q=85",
    },
    {
        "title": "Creative Artwork",
        "category": "Graphic Design",
        "description": "Striking graphics for print and digital use.",
        "image": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=1000&q=85",
    },
    {
        "title": "Custom Team Concept",
        "category": "Jersey Design",
        "description": "A unique concept made around your team's identity.",
        "image": "https://images.unsplash.com/photo-1521412644187-c49fa049e84d?auto=format&fit=crop&w=1000&q=85",
    },
    {
        "title": "Digital Design",
        "category": "Graphic Design",
        "description": "Modern visual assets for your next project.",
        "image": "https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&w=1000&q=85",
    },
]

@app.route("/")
def home():
    message = "Hello! I saw your design portfolio and would like to ask about a custom jersey or graphic design."
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
    return render_template("index.html", designs=DESIGNS, whatsapp_url=whatsapp_url)

@app.route("/order/<int:design_id>")
def order_design(design_id):
    if design_id < 0 or design_id >= len(DESIGNS):
        return "Design not found", 404
    design = DESIGNS[design_id]
    message = f"Hello! I'm interested in your design: {design['title']}. Please share details and pricing."
    return render_template(
        "redirect.html",
        whatsapp_url=f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}",
        design=design,
    )

if __name__ == "__main__":
    # For local development only. Use a production WSGI server when deploying.
    app.run(debug=True)
