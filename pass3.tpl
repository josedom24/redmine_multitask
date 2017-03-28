%include('header.tpl')
      <div class="container">

      <form class="form-signin" action="step3" method="post">
        <h2 class="form-signin-heading">Redmine Multitask</h2>
        <h3 class="form-signin-heading">Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
      </div>
      <div class="container">      

         <fieldset>
          <legend>Nueva Tarea -Proyecto:{{nombreproyecto}}</legend>

          <label for="Tittle">Título:</label>
          
          <input class="form-control" type="text" id="title" name="tittle" required>
          <label for="bio">Descripción:</label>
          <textarea rows="10" class="form-control" id="bio" name="desc" required></textarea>
        
          <label for="job">Categoría:</label>
        <select class="form-control" id="categoria" name="categoria">
         % for p in categorias:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
        </select>
                 
          <label for="date">Fecha fin:</label>
          <input class="form-control" type="text" name="fecha2" pattern="\d{1,2}/\d{1,2}/\d{4}">
          <div class="radio">
            <label>
            <input  type="radio" name="opcion" value="grupo" checked> Seleccionar por grupo<br>
            Grupos:
          </label>
          </div>
          <select class="form-control" name="grupo">
          % for p in grupos:
            <option value="{{p["id"]}}">{{p["name"]}}</option>
          % end
          </select>
          <div class="radio">
            <label>
              <input type="radio" name="opcion" value="alumno"> Seleccionar por alumnos<br>
                Alumnos:</label>
          </div>
          % for p in usuarios:
            % if p["roles"][0]["id"]==9 and p.has_key("user"):
            <div class="checkbox">
              <label>
                <input  type="checkbox" name="alumnos" value="{{p["user"]["id"]}}"> 
                {{p["user"]["name"]}}</label></div>
            % end
          % end

        
        <button class="btn btn-lg btn-primary btn-block" type="submit" >Siguiente</button>
      </fieldset>
      </form>

    </div> <!-- /container -->




      </form>
      
    </body>
</html>




