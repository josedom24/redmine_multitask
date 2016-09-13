<html>  
  <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign Up Form</title>
        
        <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="/static/main.css">
    </head>
    <body>

      <form action="step2" method="post">
      
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
    <fieldset>
          <legend><span class="number">2</span>Proyecto</legend>
          <label for="Proyecto">Proyecto:</label>
          <select name="proyecto">
          % for p in proyectos:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
          </select>
          
      <button type="submit">Siguiente</button>
      </form>
      
    </body>
</html>