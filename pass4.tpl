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

      <form action="step4" method="post">
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
        
    <fieldset>
          <legend><span class="number">4</span>Nueva Tarea - Proyecto:{{nombreproyecto}}</legend>
          <label for="Tittle">Título:</label>
          % if error.has_key("tittle"):
          <label for="Tittle">{{error["tittle"]}}</label>
          % end
          <input type="text" id="title" name="title" value="{{info["tittle"]}}">
          <label for="bio">Descripción:</label>
          <textarea id="bio" name="desc"></textarea>
        
        <label for="job">Categoría:</label>
        <select id="categoria" name="categoria">
         % for p in categorias:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
        </select>
                 
          <label for="date">Fecha fin:</label>
          <input type="text" name="fecha2" value="dd/mm/aaaa">
        </fieldset>
          <button type="submit">Crear tareas</button>
      </form>
      
    </body>
</html>