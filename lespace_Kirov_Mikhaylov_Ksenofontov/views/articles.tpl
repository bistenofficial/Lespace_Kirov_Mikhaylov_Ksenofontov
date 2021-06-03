% rebase('layout.tpl', title=title, year=year)
%import json

<head>
<title>Articles</title>
</head>
<body>
 <style>
  body {background: #000000;
  color: #FFFFFF;
  }

  </style>
    <h1>Articles</h1>
<h2> Add your own article</h2>

<form action= "/articles" method="post" style="margin-bottom: 10px">
        <p><input rows="2" cols="55" name="TITLE" placeholder="Your article's title"></p>
        <p><textarea type="text" size="55" name="DESCRIPTION" placeholder="Your article's description"></textarea></p>
        <p><input rows="2" cols="55" name="AUTHOR" placeholder="Enter your name.."></p>
        <p><input rows="2" cols="55" name="PHONE" placeholder="Enter your phone.."></p>
        <p><input rows="2" cols="55" name="AUTHOR_EMAIL" placeholder="Enter your email.."></p> 
        <p><input rows="2" cols="55" name="WRITTEN_DATE" placeholder="Date of writing of the article"></p> 
        <p><input type="submit" value="Add articl" class="btn-default"></p>
</form>
<br>
<br>
<h1 style="text-align:center"> Articles to read</h1>
%with open('articles.json') as articles:
%data=json.load(articles)
%for key, value in data.items():
    <div style="border-bottom: 3px solid LightSalmon">
        <h2 style="margin-top:50px">
        {{value["title"]}}
        </h2>
        <p style="font-size:20pt">
        {{value['description']}}
        </p>
        <p style="font-size:20pt">
        By {{value['author']}}\
        </p>
        <p style="font-size:15pt">
        Published on {{value['published_date']}}, written on {{value['written_date']}}
        </p>
        <p style="font-size:15pt">
        Email {{value['author_email']}}
        </p>
        <p style="font-size:10pt">
        Phone {{value['phone']}}
        </p>
    </div>
%end

</body>
