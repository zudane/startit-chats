from flask import jsonify


LOGFILE = "chat.log"


def get_chat():
  full_chat = []
  with open(LOGFILE, "r") as f:
    for line in f:
      full_chat.append({"message": line})
  return jsonify({"messages": full_chat})


def add_message(message):
  with open(LOGFILE, "a", newline="") as f:
    f.write(message + "\n")