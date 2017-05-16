"""This is the command of our module"""
file = open('index.html', 'r', encoding='utf-8')
template_file = file.read()
template_var = {"title": 'Some Title'}
print(template_file.format(**template_var))

file.close()

html = """
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{main_title}</h1>
    </body>
</html>
""".format(**{"title": "title", "main_title": "Main Title"})
