from flask import Flask, render_template, request
from base_datos import Ticket
from funciones_tickets import guardar_ticket, obtener_ticket_por_id, actualizar_ticket

import supabase

# Replace with your Supabase credentials
supabase_client = supabase.create_client(
    url="https://ropuxmgghlsiwqxhekww.supabase.co",
    key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJvcHV4bWdnaGxzaXdxeGhla3d3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDM3MjE0MzMsImV4cCI6MjAxOTI5NzQzM30.7gz0zqptjur7MqTK4PPadtSiRH9QnQG8KSEbrq3l6ZI"
)

app = Flask(__name__)

@app.route("/")
def index():
  tickets = obtener_tickets()

  return render_template("index.html", tickets=tickets)

@app.route("/tickets/new", methods=["GET", "POST"])
def new_ticket():
    if request.method == "GET":
        return render_template("new_ticket.html")
    else:
        equipo = request.form["equipo"]
        problema = request.form["problema"]
        fecha_creacion = request.form["fecha_creacion"]
        ticket = Ticket(equipo, problema, fecha_creacion)
        guardar_ticket(supabase_client, ticket)
        return render_template("ticket_created.html", ticket=ticket)

@app.route("/tickets/list", methods=["GET"])
def list_tickets():
    tickets = []
    results = supabase_client.table("tickets").select("*").execute()
    for row in results.data:
        tickets.append(Ticket(row["equipo"], row["problema"], row["fecha_creacion"]))
    return render_template("tickets_list.html", tickets=tickets)

@app.route("/tickets/update", methods=["GET", "POST"])
def update_ticket():
    if request.method == "GET":
        # Obtener el ticket a actualizar
        id_ticket = request.args.get("id")
        ticket = obtener_ticket_por_id(supabase_client, id_ticket)
        return render_template("update_ticket.html", ticket=ticket)
    else:
        # Actualizar el ticket en la base de datos
        id_ticket = request.form["id"]
        equipo = request.form["equipo"]
        problema = request.form["problema"]
        fecha_creacion = request.form["fecha_creacion"]
        ticket = Ticket(equipo, problema, fecha_creacion)
        ticket.id = id_ticket
        actualizar_ticket(supabase_client, ticket)
        return render_template("ticket_updated.html", ticket=ticket)

if __name__ == "__main__":
    app.run(debug=True)

