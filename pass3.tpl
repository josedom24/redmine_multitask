<!DOCTYPE html>
<html>  
  <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign Up Form</title>
        
        <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="/static/main.css">
    </head>
    <body>

      <form action="step3" method="post">
      
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
        
    <fieldset>
          <legend><span class="number">3</span>Proyecto:{{nombreproyecto}}</legend>
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




