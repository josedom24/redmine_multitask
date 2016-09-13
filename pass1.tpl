<html>  
  <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign Up Form</title>
        
        <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="/static/main.css">
    </head>
    <body>

      <form action="login" method="post">
      
        <h1>Redmine Multi Task</h1>
        
        <fieldset>
          <legend><span class="number">1</span>Autentificación</legend>
         
          % if 'error' in locals():

                <b>Usuario incorrecto</b>
          % end
          <label for="name">Usuario:</label>
          <input type="text" id="name" name="user_name">
                            
          <label for="password">Password:</label>
          <input type="password" id="password" name="user_password">
          
          
        
        
        <button type="submit">Entrar</button>
      </form>
      
    </body>
</html>