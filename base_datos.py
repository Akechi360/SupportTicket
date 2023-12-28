import supabase

# Crea una instancia del cliente Supabase (reemplaza los valores con tus credenciales)
supabase_client = supabase.create_client(
  url="https://ropuxmgghlsiwqxhekww.supabase.co", 
  api_keys="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJvcHV4bWdnaGxzaXdxeGhla3d3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDM3MjE0MzMsImV4cCI6MjAxOTI5NzQzM30.7gz0zqptjur7MqTK4PPadtSiRH9QnQG8KSEbrq3l6ZI"
)

class Ticket:
    """Representa un ticket del sistema."""

    def __init__(self, equipo, problema, fecha_creacion):
        self.equipo = equipo
        self.problema = problema
        self.fecha_creacion = fecha_creacion

def obtener_tickets():
    """Obtiene todos los tickets de la base de datos Supabase."""
    tickets = supabase_client.table("tickets").select("*").execute()

    # Crea una lista de objetos Ticket
    tickets = [Ticket(ticket["equipo"], ticket["problema"], ticket["fecha_creacion"]) for ticket in tickets.data]

    return tickets


# Obtén los tickets
tickets = obtener_tickets()

# Imprime los tickets
for ticket in tickets:
    print(ticket.equipo)
    print(ticket.problema)
    print(ticket.fecha_creacion)
