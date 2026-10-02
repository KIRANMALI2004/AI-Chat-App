from services.gemini_service import ask_gemini
from flask import Blueprint, request, jsonify
from routes.upload import last_uploaded_text
from middleware.auth import login_required
from models.chat import Chat
from models.message import Message


chat_bp = Blueprint("chat", __name__)
@chat_bp.route("/new", methods=["POST"])
@login_required
def new_chat(current_user):

    data = request.get_json()

    title = data.get("title", "New Chat")

    chat_id = Chat.create(current_user, title)

    return jsonify({

        "success": True,

        "chat_id": chat_id,

        "message": "Chat Created"

    }),201
@chat_bp.route("/", methods=["GET"])
@login_required
def all_chats(current_user):

    chats = Chat.get_all(current_user)

    response = []

    for chat in chats:

        response.append({

            "id": str(chat["_id"]),

            "title": chat["title"],

            "model": chat["model"],

            "created_at": chat["created_at"]

        })

    return jsonify({

        "success": True,

        "data": response

    })
@chat_bp.route("/<chat_id>", methods=["GET"])
@login_required
def get_chat(current_user, chat_id):

    chat = Chat.get(chat_id)

    if not chat:

        return jsonify({

            "success":False,

            "message":"Chat Not Found"

        }),404

    messages = Message.get_messages(chat_id)

    result=[]

    for message in messages:

        result.append({

            "role":message["role"],

            "content":message["content"],

            "created_at":message["created_at"]

        })

    return jsonify({

        "success":True,

        "chat":{

            "id":str(chat["_id"]),

            "title":chat["title"],

            "messages":result

        }

    })
@chat_bp.route("/<chat_id>", methods=["DELETE"])
@login_required
def delete_chat(current_user, chat_id):

    Message.delete(chat_id)

    Chat.delete(chat_id)

    return jsonify({

        "success":True,

        "message":"Chat Deleted"

    })
    
@chat_bp.route("/message", methods=["POST"])
@login_required
def save_message(current_user):

    data = request.get_json()

    Message.create(

        data["chat_id"],

        "user",

        data["message"]

    )

    return jsonify({

        "success":True,

        "message":"Saved"

    })
    
@chat_bp.route("/ask", methods=["POST"])
@login_required
def ask_ai(current_user):
    data = request.get_json()

    print("Received:", data)

    prompt = data.get("message")

    reply = ask_gemini(
    prompt,
    last_uploaded_text
    )

    print("Gemini Reply:", reply)

    return jsonify({
        "success": True,
        "reply": reply
    }), 200