%include('header.tpl')
      <form action="login" method="get">
        <h1>Redmine Multi Task</h1>
        <h3>Usuario:{{user}}</h3><p><a href="logout">Salir</a></p>
        
    <fieldset>
          <legend><span class="number">4</span>Nueva Tarea - Proyecto:{{nombreproyecto}}</legend>
          <label for="Tittle">{{!resultado}}</label>
                 </fieldset>
         
          

          <button type="submit">Terminar</button>
      </form>
      
    </body>
</html>