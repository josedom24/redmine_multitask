%include('header.tpl')
      <div class="container">

      <form class="form-signin" action="login" method="get">
        <h2 class="form-signin-heading">Redmine Multitask</h2>
        <h3 class="form-signin-heading">Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>

         <fieldset>
          <legend>Nueva Tarea -Proyecto:{{nombreproyecto}}</legend>
          <label for="Tittle">{{!resultado}}</label>
         </fieldset>
         
        <button class="btn btn-lg btn-primary btn-block" type="submit" >Terminar</button>
      </form>

    </div> <!-- /container -->


      
    </body>
</html>