print("""
<!DOCTYPE html>
<html>
<body>
<table>
"""
)

with open("texto.txt") as f:
    lines = f.readlines()
    for line in lines:
        print("<tr>")
        columns = line.split("), (")
        for column in columns[1:-1]:
            print(f'<td style="background-color: rgb({column})" ></td>')
        print("</tr>")
            
            
print("""
</table>
</body>
</html>
"""
)