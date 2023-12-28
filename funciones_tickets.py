from base_datos import conectar_base_datos

import supabase  # Importa la biblioteca Supabase

# ... (resto del código de funciones_tickets.py)

def actualizar_ticket(supabase_client, ticket):
    """Actualiza un ticket en la base de datos Supabase."""
    supabase_client.table("tickets").update({
        "equipo": ticket.equipo,
        "problema": ticket.problema,
        "fecha_creacion": ticket.fecha_creacion
    }).eq("id", ticket.id).execute()

class Ticket:
  """Representa un ticket."""

  def __init__(self, equipo, problema, fecha_creacion):
    self.equipo = equipo
    self.problema = problema
    self.fecha_creacion = fecha_creacion

def guardar_ticket(supabase_client, ticket):
  """Guarda un ticket en la base de datos."""
  connection = conectar_base_datos()
  cursor = connection.cursor()

  sql = "INSERT INTO tickets (equipo, problema, fecha_creacion) VALUES (?, ?, ?)"

  cursor.execute(sql, (ticket.equipo, ticket.problema, ticket.fecha_creacion))

  connection.commit()

def obtener_ticket_por_id(supabase_client, id_ticket):
  """Obtiene un ticket de la base de datos por su ID."""
  connection = conectar_base_datos()
  cursor = connection.cursor()

  sql = "SELECT * FROM tickets WHERE id=?"

  cursor.execute(sql, (id_ticket,))

  ticket = None
  for row in cursor:
    ticket = Ticket(row[0], row[1], row[2])

  return ticket
