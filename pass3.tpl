%include('header.tpl')
      <form action="step3" method="post">
      
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
        
    <fieldset>
          <legend><span class="number">3</span>Nueva Tarea -Proyecto:{{nombreproyecto}}</legend>


          <label for="Tittle">Título:</label>
          
          <input type="text" id="title" name="tittle" required>
          <label for="bio">Descripción:</label>
          <textarea id="bio" name="desc" required></textarea>
        
        <label for="job">Categoría:</label>
        <select id="categoria" name="categoria">
         % for p in categorias:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
        </select>
                 
          <label for="date">Fecha fin:</label>
          <input type="text" name="fecha2" pattern="\d{1,2}/\d{1,2}/\d{4}">

          <input type="radio" name="opcion" value="grupo" checked> Seleccionar por grupo<br>
          <label for="Proyecto">Grupos:</label>
          <select name="grupo">
          % for p in grupos:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
          </select>
          <input type="radio" name="opcion" value="alumno"> Seleccionar por alumnos<br>
          <label for="Proyecto">Alumnos:</label>
          % for p in usuarios:
            % if p["roles"][0]["id"]==9 and p.has_key("user"):
              <input type="checkbox" name="alumnos" value="{{p["user"]["id"]}}"> {{p["user"]["name"]}}<br>
            % end
          % end
      <button type="submit">Siguiente</button>
      </form>
      
    </body>
</html>




