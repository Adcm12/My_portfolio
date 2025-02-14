import sqlite3
import datetime

class AdministradorTareas:

    def __init__(self, nombre_db="tareas.db"):
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def __str__(self):
        return f"Nro de tarea: {self.id}\n" \
               f"Tarea: {self.tarea}\n" \
               f"Fecha de inicio: {self.fecha_inicio}\n" \
               f"Fecha de vencimiento: {self.fecha_vencimiento}\n" \
               f"Fecha de finalizacion: {self.fecha_finalizacion if self.fecha_finalizacion else 'Pendiente'}"

    def crear_tabla(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarea TEXT NOT NULL,
                fecha_inicio TEXT NOT NULL,
                fecha_vencimiento TEXT NOT NULL,
                fecha_finalizacion TEXT,
                descripcion TEXT
            )
        """)
        self.conexion.commit()

    def crear_tarea(self, tarea, fecha_vencimiento, descripcion=None):

        fecha_inicio = datetime.date.today().strftime("%d/%m/%Y")
        self.cursor.execute("""
            INSERT INTO tareas (tarea, fecha_inicio, fecha_vencimiento, fecha_finalizacion, descripcion)
            VALUES (?, ?, ?, ?, ?)
        """, (tarea, fecha_inicio, fecha_vencimiento, None, descripcion))
        self.conexion.commit()
        return self.cursor.lastrowid

    def leer_tarea(self):
        self.cursor.execute("SELECT * FROM tareas")
        tareas = self.cursor.fetchall()
        tareas_obj = []
        for tarea in tareas:
            tarea_obj = AdministradorTareas()
            tarea_obj.id = tarea[0]
            tarea_obj.tarea = tarea[1]
            tarea_obj.fecha_inicio = tarea[2]
            tarea_obj.fecha_vencimiento = tarea[3]
            tarea_obj.fecha_finalizacion = tarea[4]
            tareas_obj.append(tarea_obj)
        return tareas_obj
        

    def actualizar_tarea(self, id_tarea, tarea=None, fecha_vencimiento=None, fecha_finalizacion=None, descripcion=None):
        campos_actualizar = []
        valores_actualizar = []
        if tarea:
            campos_actualizar.append("tarea = ?")
            valores_actualizar.append(tarea)
        if fecha_vencimiento:
            campos_actualizar.append("fecha_vencimiento = ?")
            valores_actualizar.append(fecha_vencimiento)
        if fecha_finalizacion:
            campos_actualizar.append("fecha_finalizacion = ?")
            valores_actualizar.append(fecha_finalizacion)
        if descripcion:
            campos_actualizar.append("descripcion = ?")
            valores_actualizar.append(descripcion)

        if not campos_actualizar:
            return False

        sql = f"""
            UPDATE tareas
            SET {', '.join(campos_actualizar)}
            WHERE id = ?
        """
        valores_actualizar.append(id_tarea)

        self.cursor.execute(sql, tuple(valores_actualizar))
        self.conexion.commit()
        return self.cursor.rowcount > 0
    
    def finalizar_tarea(self, id_tarea):
        fecha_finalizacion = datetime.date.today().strftime("%d/%m/%Y")
        self.cursor.execute("""
            UPDATE tareas
            SET fecha_finalizacion = ?
            WHERE id = ?
        """, (fecha_finalizacion, id_tarea))
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def borrar_tarea(self, id_tarea):
        self.cursor.execute("""
            DELETE FROM tareas WHERE id = ?
        """, (id_tarea,))
        self.conexion.commit()
        return self.cursor.rowcount > 0

    def cerrar(self):
        self.conexion.close()
