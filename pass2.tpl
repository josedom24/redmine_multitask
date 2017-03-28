%include('header.tpl')
      
      <div class="container">

      <form class="form-signin" action="step2" method="post">
        <h2 class="form-signin-heading">Redmine Multitask</h2>
        <h3 class="form-signin-heading">Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>

         <label>Proyecto:</label>

        <select name="proyecto" class="form-control">
          % for p in proyectos:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
          </select>
        
        <button class="btn btn-lg btn-primary btn-block" type="submit" >Siguiente</button>
      </form>

    </div> <!-- /container -->


      
    </body>
</html>