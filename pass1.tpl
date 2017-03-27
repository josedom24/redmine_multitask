%include('header.tpl')
     
    <div class="container">

      <form class="form-signin" action="login" method="post">
        <h2 class="form-signin-heading">Redmine Multitask</h2>
        % if 'error' in locals():

                <b>Usuario incorrecto</b>
          % end

         <label for="inputEmail" class="sr-only">Usuario:</label>
        <input type="text" id="inputEmail" class="form-control" name="useer_name" placeholder="Ususario" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" id="inputPassword" class="form-control" name="user_password" placeholder="Password" required>

        <button class="btn btn-lg btn-primary btn-block" type="submit" >Sign in</button>
      </form>

    </div> <!-- /container -->



      
    
      
    </body>
</html>