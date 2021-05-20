% rebase('layout.tpl', title=title, year=year)
% import Organiz
 
<html>
  <head>
    <meta charset="utf-8">
   <style>
    body {background: #000000;
    color: #FFFFFF;
    }
    </style>
  <head>
  <h2>Partner</h2>
  <h3> New partner </h3>
  <form action="/home1" method="post"> <!--Три поля для ввода и кнопка для добавления партнера -->
        <p><input type="text" size="50" name="NAME" placeholder="Name organization"></p>
        <p><input type="text" size="50" name="Telep" placeholder="Telephone"></p>
        <p><textarea rows="2" cols="50" name="DESC" placeholder="Description"></textarea></p> 
        <p><input type="submit" value="Entry"  class="btn btn-default". ></p>
  </form>

  <div>
   <h3> Our partners </h3>  <!--Часть для вывода существующих партнеров -->
   <form>
     %Organ = Organiz.get_all_organization()
     %for organiz in Organ:
     <div>
      <h1>{{organiz['Name']}}</h1>
      <p>{{organiz['Telephone']}}</p>
      <p>{{organiz['Description']}}</p>
     </div>
     %end
   </form>
  </div>
</html>