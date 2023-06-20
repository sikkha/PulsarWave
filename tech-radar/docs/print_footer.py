def append_footer(file_path):
    footer = '''    {
        "quadrant": 3,
        "ring": 1,
        "label": "RabbitMQ",
        "link": "https://engineering.zalando.com/tags/rabbitmq.html",
        "active": true,
        "moved": 0
      }

]
  //ENTRIES
});

</script>

<table>
<tr>
<td>
</td></tr>
</table>

</body>
</html>

'''

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(footer)

# Example usage:
file_path = 'new_index.html'
append_footer(file_path)

