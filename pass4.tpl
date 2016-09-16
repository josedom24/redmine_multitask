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

      <form action="login" method="get">
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
        
    <fieldset>
          <legend><span class="number">4</span>Nueva Tarea - Proyecto:{{nombreproyecto}}</legend>
          <label for="Tittle">{{resultado}}</label>
                 </fieldset>
         
          

          <button type="submit">Terminar</button>
      </form>
      
    </body>
</html>