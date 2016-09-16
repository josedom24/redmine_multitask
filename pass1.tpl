%include('header.tpl')
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